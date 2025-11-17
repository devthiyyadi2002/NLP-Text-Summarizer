import os 
import sys
import logging 

# creating a log directory 
log_dir = "logs"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# creating a logging file path 
log_file_path = os.path.join(log_dir,"continous_logs.log")

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_file_path), # log file path logs the messages in the particular folder we chose
        logging.StreamHandler(sys.stdout) # displays all the logs in the output terminal 
    ]
)

logger = logging.getLogger("SummarizerLogger")