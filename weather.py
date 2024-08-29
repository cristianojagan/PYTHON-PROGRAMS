import requests
import os
from dotenv import load_dotenv

load_dotenv()

def LatestWeather():
    print(f"\nLatest Weather Reports\n")
    city=input("Please enter the city: ")
    url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    request=requests.get(url).json()
    print(request)

if __name__=="__main__":
    LatestWeather()