import logging
from . import summ
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    

    name = req.params.get('name')
    
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        
        v1 = int(req.params.get('v1'))
        v2 = int(req.params.get('v2'))
        logging.info(f'Calculating the sum values for the given input {v1} and {v2}')
        val = summ.add(v1,v2)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. {val}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
