#print hello world in python
print("Hello, World!")

#read environment variables
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom  # For pretty printing XML
import json
import csv
import logging
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

#load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#load local file path from environment variable
LOCAL_FILE_PATH = os.getenv('DATA_PATH')

#run the script to print the local file path
logger.info(f"Local file path: {LOCAL_FILE_PATH}")

#read the file and print the lines
def read_file(file_path):
    try:
        logger.info("Reading the data file...")
        with open(file_path, 'r') as file:
            lines = file.readlines()
            #skip the header line(1st line) 
            for line in lines[1:]:
                if line.strip():  # Check if the line is not empty
                    print(line.strip())
        logger.info("Reading the data file...")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

#if__name__ == "__main__":

if __name__ == "__main__":
    read_file(LOCAL_FILE_PATH) 