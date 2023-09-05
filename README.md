# WeatherApp
This is a GUI for a weather application made in Python; Uses ttkbootstrap for the GUI and RapidAPI for the Weather Data  
<br>
## You must provide your own API keys
The API keys in this repository are stored locally with my RapidAPI account. To use this personally, you must:
- Have a RapidAPI account
- Have a "keys.py" that contains your API key in the following format:
  - headers = {
	    "X-RapidAPI-Key": "APIKEY",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
  - Note: Keep the host since this is the API that I use for the Weather Data

From there, the application should work fine from there since the "keys.py" that is created is already imported in the main file (weatherapp.py)

![Weather App - StartUp](/images/Weather%20App%20-%20StartUp.png)

![Weather App - Submitting User Input](/images/Weather%20App%20-%20Submitting%20User%20Input.png)

## ENJOY!
