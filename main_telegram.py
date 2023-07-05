import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Hello! Please enter the name of the city and I will inform you about the current weather conditions.')
@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        'Clear': 'Clear \U0001F31E',
        'Clouds': 'Clouds \U0001F324',
        'Rain': 'Rain \U0001F327',
        'Drizzle': 'Drizzle \U0001F32B',
        'Thunderstorm': 'Thunderstorm \U0001F329',
        'Snow': 'Snow \U0001F328',
        'Mist': 'Mist \U0001F32B'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        weather_descriptionc = data['weather'][0]['main']
        if weather_descriptionc in code_to_smile:
            wd = code_to_smile[weather_descriptionc]
        else:
            wd = 'Good luck!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        await message.reply (f'Current date and time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}   \n'
              f'Weather in city: {city}\nTemperature: {cur_weather} °C - {wd}\n'
              f'Humidity: {humidity} %\nPressure: {pressure} mbar\nWind: {wind} kph\n'
              f'Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of day: {length_of_the_day}\n'
              f'Have a good day!'
              )
    except:
        await message.reply('Please check if name of city is correct')

if __name__ == '__main__':
    executor.start_polling(dp)