import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import requests
import weather
import soil
# import crop_disease
import planting

app = FastAPI()

# Define a data model to parse incoming webhook requests


# class WebhookRequest(BaseModel):
#     responseId: str
#     queryResult: dict
#     session: str
#     ...


# Main webhook handler

@app.post("/")
async def root(request : Request):
    # Parse the incoming webhook request
    # try:
    #     # Parse the incoming webhook request
    #     print(f"entering request {request}")
    webhook_request = await request.json()
    #     return {"fulfillmentText" : f"{webhook_request}"}
    # except json.JSONDecodeError as e:
    #     return JSONResponse(status_code=405, content={"fulfillmentText": str(e)})
    query_result = webhook_request.get('queryResult')
    intent_name = query_result.get('intent').get('displayName')
    parameters = query_result.get('parameters')
    session_id = webhook_request.get('session')

#    # Route the request to the appropriate function based on the intent
    if intent_name == 'Weather':
        response = weather.handle_weather_intent(parameters, session_id)
    elif intent_name == 'Soil_Inputs-context:soil':
        response = soil.handle_soil_quality_intent(parameters, session_id)
    # elif intent_name == 'crop_disease_prediction':
    #     response = crop_disease.handle_crop_disease_intent(
    #         parameters, session_id)
    elif intent_name == 'Planting_times':
        response = planting.handle_planting_intent(parameters, session_id)
    else:
        response = {
            "fulfillmentText": "Sorry, intent not recognized. Please try again"}

    return JSONResponse(content=response)

# Run the FastAPI app
# if __name__ == "__main__":
#     uvicorn.run(app)