import requests
import datetime

run = True
API_key = "2cd85850a86bfaf380990c1ed61b1d99"
while run:
    city_name = input("Enter the City Name: ")
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_key}&units=metric")
    if data.json()['cod'] == 200:
        Weather = data.json()['weather'][0]['main']
        temp = data.json()['main']['temp']
        feels_like = data.json()['main']['feels_like']
        temp_min = data.json()['main']['temp_min']
        temp_max = data.json()['main']['temp_max']
        humidity = data.json()['main']['humidity']
        wind_speed = data.json()['wind']['speed']
        wind_speed_kmph = wind_speed*3.6
        wind_pressure = data.json()['main']['pressure']
        sunset_unix = data.json()['sys']['sunset']
        sunrise_unix = data.json()['sys']['sunrise']
        sunrise = datetime.datetime.fromtimestamp(sunrise_unix).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(sunset_unix).strftime('%H:%M')
        Country = data.json()['sys']['country']
        City = data.json()['name']
        print(f"{City} , {Country}")
        print("Weather: ", Weather)
        print(f"Temperature: {temp}°C")
        print(f"Max Temperature: {temp_max}°C , Minimum Temprature: {temp_min}°C")
        print(f"It feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed_kmph}kmph, Wind Pressure: {wind_pressure}hPa")
        print("Sunset: " , sunset)
        print("Sunrise: ", sunrise)
    else:
        print("Invalid City")
    response = input("Would you like to Search Another City?(y/n) : ")
    if(response.lower() == "y"):
        run = True
    else:
        run = False
print("Thank you for Using!!")