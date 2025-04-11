# import mysql.connector
from datetime import datetime

# Define a function to handle the "optimal planting times" intent
def handle_planting_intent(params, session_id):
    # Extract parameters from 'params' dictionary
    # crop = params.get('crop').capitalize()
    # location = params.get('geo-country').capitalize()

    # # Initializing mySQL server
    # db_config = {
    #     "host": "localhost",
    #     "user": "root",
    #     "password": "root",
    #     "database": "sih_project_1491",
    # }
    # conn = mysql.connector.connect(**db_config)
    # cursor = conn.cursor(dictionary=True)

    # search_query = "SELECT * FROM planting_times WHERE Location = %s AND Crop = %s"

    # cursor.execute(search_query, (location, crop))

    # results = cursor.fetchall()

    # cursor.close()
    # conn.close()

    # dates = ["Plant_start_date", "Plant_end_date", "Harvest_start_date", "Harvest_end_date"]

    # new_dates = []

    # if results:
    #     for key in dates:
    #         date_object = datetime.strptime(results[0][key], "%Y-%m-%d")
    #         new_dates.append(f"{date_object.strftime('%d')}-{date_object.strftime('%b')}")
    # else:
        # return {"fulfillmentText": "Sorry, no matching records found. Please try a different combination of crop and location"}

    

    # Return the pest and planting response
    return {"fulfillmentText": f"The optimal planting time is from to and harvesting can be done between and "}