import requests
from keys import headers
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

url = "https://weatherapi-com.p.rapidapi.com/current.json"

# Creating Window
root = tb.Window(themename="superhero")
root.title("Weather App")
root.geometry('800x600')

# Fetches Weather Data from API and returns a list
def getWeatherData(jsonData):

    locationData = jsonData.get("location")
    currentWeather = jsonData.get("current")

    city = locationData.get("name")
    province = locationData.get("region")
    country = locationData.get("country")  
    localTime = locationData.get("localtime")
    tempCelsius = currentWeather.get("temp_c")
    humidity = currentWeather.get("humidity")
    feelsLikeTemp = currentWeather.get("feelslike_c")

    weatherData = [city, province, country, localTime, tempCelsius, humidity, feelsLikeTemp]

    return weatherData

# Prints the Weather Data to the screen once the user input is submitted
stringData = ""
def printWeatherData():
    global stringData
    counter = 0
    fields = ["City: ", "Province/State: ", "Country: ", "localTime: ", "Temp (C): ", "Humidity: ", "Feels like (C): "]
    querystring = {"q": myEntry.get()}
    response = requests.get(url, headers=headers, params=querystring)
    weatherData = getWeatherData(response.json())
    for i in weatherData:
        stringData += fields[counter] + str(i) + "\n"
        counter += 1

    myLabel.config(text=stringData)

    stringData = ""

# Labels in ttkbootstrap
myLabel = tb.Label(text="Weather Data", 
                   font=("Helvetica", 14), 
                   bootstyle=DEFAULT)
myLabel.pack(pady=50)

myEntry = tb.Entry(root, bootstyle="default", 
                   font=("Helvetica", 16),
                   foreground="white",
                   width=56)
myEntry.pack(pady=30)

# Buttons in ttkbootstrap
myButton = tb.Button(text="Submit", bootstyle="SUCCESS, OUTLINE", command=printWeatherData)
myButton.pack(pady=20)

root.mainloop()