# lambda_function.py

import json
from app import app  # Assuming your FastAPI app instance is in app.py

def lambda_handler(event, context):
    if event.get("httpMethod") == "POST":
        # You can define your own event format and handling logic here
        # The event could contain the request body, headers, etc.
        response = app(event, context)  # Invoke the FastAPI app
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response),
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid HTTP method"}),
        }
