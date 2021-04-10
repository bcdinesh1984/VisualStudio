import logging
import csv
import json
import os

import azure.functions as func



def main(msg: func.QueueMessage, inputblob: func.InputStream, outputblob: func.Out[func.InputStream]) -> None:

    blob_source_raw_name = msg.get_body().decode('utf-8')
    logging.info('Python queue trigger function processed a queue item: %s', blob_source_raw_name)  

    a= inputblob.read()
    logging.info('File Name and Path: %s', a) 
    outputblob.set(a) 
    

   

