import sys
import os
import logging

class Logger:
    def __init__(self, filename):
        logger = logging.getLogger(f"{filename}_Logger")
        logger.setLevel(logging.DEBUG)
        self.logger = logger
        
        # Change directory to allow for use of relative paths
        os.chdir(os.path.dirname(__file__))
        
        # Create handlers
        file_handler_info = logging.FileHandler(f"../../Logs/{filename}_info.log")
        file_handler_debug = logging.FileHandler(f"../../Logs/{filename}_debug.log")
        stream_handler = logging.StreamHandler(sys.stdout)
        
        # Set additional log level in handlers
        file_handler_info.setLevel(logging.INFO)
        file_handler_debug.setLevel(logging.DEBUG)
        stream_handler.setLevel(logging.INFO)
        
        # Create formatter and associate with handlers
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler_info.setFormatter(formatter)
        file_handler_debug.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        
        # Add handlers to the loggers
        logger.addHandler(file_handler_info)
        logger.addHandler(file_handler_debug)
        logger.addHandler(stream_handler)
        
        # Set the info logger for initializing the script
        logger.info(f"{'#'*15} INITIALIZING THE SCRIPT {'#'*15}")
    
    def info(self, message):
        self.logger.info(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def critical(self, message):
        self.logger.critical(message)
    
    def script_completed(self):
        self.logger.info(f"{'#'*15} SCRIPT COMPLETED {'#'*15}")