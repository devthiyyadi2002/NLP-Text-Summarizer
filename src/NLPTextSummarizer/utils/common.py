# add common important functionalities 

import os 
from box.exceptions import BoxValueError # used to handle box exceptions 
import yaml 
from src.NLPTextSummarizer.logging import logger 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any 

@ensure_annotations # this function is used to reaed yaml files 
def read_yaml(path_to_yaml: Path) ->ConfigBox: # ensure annotation is used to make sure that the data passed is of the predefined data type or it will throw an error
    """ reads yaml file and returns 

    Args:
        path_to_yaml (Path): path like input 
        
    Raises: 
        ValueError : if yaml file is empty
        e : empty file
    
    Returns:
        ConfigBox: ConfigBox type 
        
        The primary use of ConfigBox is to make your life easier by allowing you to access dictionary keys using dot notation (e.g., data.key) instead of the standard dictionary syntax (e.g., data['key']).
    """
    
    try:
        with open(path_to_yaml) as yaml_file: 
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e 
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ create a list of directories

    Args:
        path_to_directories (list): list of path to directories 
        verbose (bool, optional): ignore if multiple dirs is to e created. 
    """
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose: 
            logger.info(f"created directory at : {path}")
            