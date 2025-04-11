import pickle
import numpy as np

# Define a function to handle the "soil quality prediction" intent

def handle_soil_quality_intent(params, session_id):
    # Extract parameters from 'params' dictionary

    soil_type = params.get('soil-content')
    values = params.get('number')

    # preparing the input vector

    list_of_features = ['N', 'P', 'K', 'pH', 'EC',
                        'OC', 'S', 'Zn', 'Fe', 'Cu', 'Mn', 'B']
    try:
        X = np.array([values[soil_type.index(i)]
                     for i in list_of_features]).reshape(1, -1)
    except Exception:
        return {"fulfillmentText": "Unknown error. Please try again"}

    #implementing the model

    # with open("./Models/soil_predictor.pkl", "rb") as model_file:
    #     soil_model = pickle.load(model_file)

    # model_file.close()

    # output = soil_model.predict(X)
    output = 2

    if output == 0:
        result = 'low'
    elif output == 1:
        result = 'moderate'
    elif output == 2:
        result = 'high'

    # Return the soil quality prediction response
    return {"fulfillmentText": f"The predicted soil quality is {result}."}