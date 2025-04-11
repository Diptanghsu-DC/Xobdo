from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import requests

model_name = "facebook/blenderbot-400M-distill"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

app = FastAPI()

# Define a data model to parse incoming webhook requests


# class WebhookRequest(BaseModel):
#     responseId: str
#     queryResult: dict
#     session: str
#     ...


# Main webhook handler
    
conversation_history = []

@app.post("/")
async def root(request: Request):
    # Parse the incoming webhook request
    webhook_request = await request.json()
    query_result = webhook_request.get('queryResult')
    intent_name = query_result.get('intent').get('displayName')
    parameters = query_result.get('parameters')
    session_id = webhook_request.get('session')
    text_prompt = query_result.get('queryText')

   # Route the request to the appropriate function based on the intent
    if intent_name == 'Default Fallback Intent':
        # Create conversation history string
        history_string = "\n".join(conversation_history)

        # Get the input data from the user #when testing prototype
        #input_text = input("> ")
        input_text = text_prompt

        # Tokenize the input text and history
        inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

        # Generate the response from the model
        outputs = model.generate(**inputs, max_length=60)

        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Add interaction to conversation history
        conversation_history.append(input_text)
        conversation_history.append(response)

        response = {
            "fulfillmentText": response}
    else:
        response = {
            "fulfillmentText": "Sorry, intent not recognized. Please try again"}

    return JSONResponse(content=response)

# Run the FastAPI app
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)