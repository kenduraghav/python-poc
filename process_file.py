import os
import glob
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants from the environment
ACCESS_TOKEN_URL = os.getenv("ACCESS_TOKEN_URL")
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
DATA_PATH = os.getenv("DATA_PATH")
RETRY_LIMIT = int(os.getenv("RETRY_LIMIT", 5))

# Create the folder for failed records if it doesn't exist
FAILED_RECORDS_FOLDER = "failed_records"
os.makedirs(FAILED_RECORDS_FOLDER, exist_ok=True)

# Function to get the access token
def get_access_token():
    logger.info("Requesting access token...")
    response = requests.post(ACCESS_TOKEN_URL, data={"api_key": API_KEY})
    if response.status_code == 200:
        token = response.json().get("access_token")
        logger.info("Access token retrieved successfully.")
        return token
    else:
        logger.error(f"Failed to get access token: {response.status_code}")
        return None

# Retry logic for posting data
@retry(stop=stop_after_attempt(RETRY_LIMIT), wait=wait_exponential(multiplier=1, min=4, max=10))
def post_to_api(xml_data, token):
    logger.info("Posting data to API...")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/xml"}
    response = requests.post(API_URL, data=xml_data, headers=headers)

    if response.status_code == 200:
        logger.info("Data posted successfully.")
        return True
    else:
        logger.error(f"Failed to post data, status code: {response.status_code}")
        return False

# Function to convert row data to XML
def convert_to_xml(data):
    root = ET.Element("events")
    for row_data in data:
        tid, event, name, street, postalcode, city, country, date = row_data
        event_element = ET.SubElement(root, "event")
        ET.SubElement(event_element, "tid").text = tid
        ET.SubElement(event_element, "event_name").text = event
        ET.SubElement(event_element, "name").text = name
        address = ET.SubElement(event_element, "address")
        ET.SubElement(address, "street").text = street
        ET.SubElement(address, "postalcode").text = postalcode
        ET.SubElement(address, "city").text = city
        ET.SubElement(address, "country").text = country
        ET.SubElement(event_element, "date").text = date

    return ET.tostring(root, encoding="unicode", method="xml")

# Function to process each file
def process_file(file_path):
    try:
        # Read the file, skipping the header
        with open(file_path, "r") as file:
            lines = file.readlines()[1:]  # Skip the first line (header)
        
        # Convert rows into XML and attempt to post them
        data = [line.strip().split(";") for line in lines]
        xml_data = convert_to_xml(data)

        token = get_access_token()
        if token:
            if not post_to_api(xml_data, token):
                # Save failed records to the failed_records folder
                failed_file_path = os.path.join(FAILED_RECORDS_FOLDER, os.path.basename(file_path))
                with open(failed_file_path, "w") as failed_file:
                    failed_file.write(xml_data)
                logger.info(f"Failed data saved to: {failed_file_path}")
        else:
            logger.error("No token available. Skipping file posting.")
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")

# Function to process all files in the DATA_PATH folder
def process_all_files():
    files = glob.glob(os.path.join(DATA_PATH, "*.txt"))
    if not files:
        logger.warning("No files found in the data directory.")
        return
    
    for file_path in files:
        logger.info(f"Processing file: {file_path}")
        process_file(file_path)

# Function to process failed records stored in failed_records/ folder
def process_failed_records():
    failed_files = glob.glob(os.path.join(FAILED_RECORDS_FOLDER, "*.xml"))
    if not failed_files:
        logger.warning("No failed records found.")
        return

    for failed_file in failed_files:
        logger.info(f"Processing failed file: {failed_file}")
        
        # Read the failed XML data
        with open(failed_file, "r") as file:
            xml_data = file.read()
        
        # Retry posting the failed XML data
        token = get_access_token()
        if token:
            if post_to_api(xml_data, token):
                # If successful, remove the failed file
                os.remove(failed_file)
                logger.info(f"Successfully retried and removed: {failed_file}")
            else:
                logger.error(f"Failed to retry posting: {failed_file}")
        else:
            logger.error("No token available. Skipping failed record.")

# Main function to start the processing
if __name__ == "__main__":
    # Process new files first
    process_all_files()

    # After processing new files, process any failed records
    process_failed_records()
