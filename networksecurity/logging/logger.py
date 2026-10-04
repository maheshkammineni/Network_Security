
import logging
import os
from datetime import datetime

# Generate a log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory path
logs_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Create the complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)

# Test the logging configuration
logging.info("Logging has started successfully.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")

print(f"Log file created at: {LOG_FILE_PATH}")