import logging
import os
from datetime import datetime

#Constants
PROGRAM_START_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
LOG_FILE_NAME = 'app'
LOG_FILE_FOLDER = 'logs' #Leave empty for no folder 
LOG_FILE_PATH = f"{LOG_FILE_FOLDER}{'/' if LOG_FILE_FOLDER and not LOG_FILE_FOLDER.endswith('/') else ''}{LOG_FILE_NAME}{'' if LOG_FILE_NAME.endswith('.log') else '.log'}"

#Create logging folder if it doesn't exist
if not os.path.exists(LOG_FILE_FOLDER):
    os.makedirs(LOG_FILE_FOLDER)


#Custom formatter to include program start time and time of logging
class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.program_start_time = f'program start time: {PROGRAM_START_TIME}'
        record.log_time = f"time at log: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        return super().format(record) #Call the original format method

formatter = CustomFormatter('%(program_start_time)s - %(log_time)s - %(levelname)s - %(message)s')

#Console handler for all log levels
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG) #Change level to change logging behaviour (see levels at bottom)
console_handler.setFormatter(formatter)

#File handler for warnings and above
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.WARNING) #Change level to change logging behaviour (see levels at bottom)
file_handler.setFormatter(formatter)

#Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler) #Logging to console
logger.addHandler(file_handler) #Loggin to a .log file

#Test
if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")