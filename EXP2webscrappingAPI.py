import requests

# API to fetch temperature of a city
city_name = input("Enter the city name: ")
api_key = "2f8344b11e619f0341a72d0ba0753cc2"  # Your OpenWeather API key

# Build URL for the API
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

# Get information from the server
get_server_information = requests.get(api_url)

# Check if the request was successful
if get_server_information.status_code == 200:
    # Convert response to JSON format
    weather_data = get_server_information.json()
    
    # Extracting the temperature and weather description
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    
    # Display the output
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather Description: {weather_description.capitalize()}")
else:
    # Display error if the API call fails
    print(f"Failed to retrieve data. Status Code: {get_server_information.status_code}")
    print("Reason:", get_server_information.json().get('message', 'No message from server'))
