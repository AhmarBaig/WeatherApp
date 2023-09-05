import requests
import tkinter 


url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Toronto"}

headers = {
	"X-RapidAPI-Key": "8ed1746f1bmshb84dd11a6694a7cp1bed5ajsn44f54e38d5a5",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

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

def printWeatherData():
    weatherData = getWeatherData(response.json())

    label = tkinter.Label(window, text=weatherData)

    # print("City = {}".format(weatherData[0]))
    # print("Province = {}".format(weatherData[1]))
    # print("Country = {}".format(weatherData[2]))
    # print("localtime = {}".format(weatherData[3]))
    # print("Temp (C) = {}".format(weatherData[4]))
    # print("Humidity = {}".format(weatherData[5]))
    # print("Feels like (C) = {}".format(weatherData[6]))

    label.grid(column=2, row=3)
    
window = tkinter.Tk()
# window.geometry("500x500")

b = tkinter.Button(window, text="Display Weather Data", command=printWeatherData)
b.grid(column=2, row=2)

window.mainloop()



