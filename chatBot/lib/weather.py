import requests

def get_weather(api_key, city_name):
    # Define the OpenWeatherMap API endpoint
    api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
    
    # Define the parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change the units (metric, imperial) as needed
    }

    try:
        # Make the API request
        response = requests.get(api_endpoint, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            # Extract and format the weather information
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            # Construct the weather response
            weather_response = f"Weather in {city_name}: {weather_description}, Temperature: {temperature}°C, Humidity: {humidity}%"
            return weather_response
        else:
            return "Unable to fetch weather information. Please try again later."

    except Exception as e:
        return str(e)

# Define a function to handle the "display weather" intent
def handle_weather_intent(params, session_id):
    # Extract parameters from 'params' dictionary
    location = params.get('location').get('city')

    # Use OpenWeatherMap API to fetch weather data based on 'location'
    api_key = "db57d2afeced9827ac3dd4a613e01513"
    city_name = location  # Replace with the desired city name

    weather_data = get_weather(api_key, city_name)

    # Return the weather response
    return {"fulfillmentText": weather_data}