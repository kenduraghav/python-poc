import subprocess
import time
import os
import json
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pynotifier import Notification
from livereload import Server

# Load configuration from the config file
def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

# Get the docs folder from config
config = load_config()
DOCS_FOLDER = config.get("docs_folder", "docs")
MAIN_FILE = os.path.join(DOCS_FOLDER, "main.adoc")
OUTPUT_FILE = os.path.join(DOCS_FOLDER, "main.html")

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith((".adoc", ".html")):
            print(f"🔄 Change detected in {event.src_path} — Recompiling {MAIN_FILE}...")
            compile_and_notify()

def compile_and_notify():
    subprocess.run(["asciidoctor", MAIN_FILE])
    print(f"✅ Compiled {MAIN_FILE} to {OUTPUT_FILE}")
    
    # Auto open in default web browser if not already open
    if not is_browser_open():
        webbrowser.open(OUTPUT_FILE)

    # Show a system tray notification
    Notification(
        title='AsciiDoc Compilation',
        description=f'{MAIN_FILE} has been compiled to {OUTPUT_FILE}!',
        duration=5  # Duration in seconds
    ).send()

 
# Check if the browser is already open
def is_browser_open():
    try:
        with open(os.devnull, 'w') as null:
            subprocess.call(["pgrep", "chrome"], stdout=null, stderr=null)
            return True
    except Exception:
        return False



if __name__ == "__main__":
    # Start the LiveReload server

    print(f"👀 Watching for changes in {DOCS_FOLDER}...")
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DOCS_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
