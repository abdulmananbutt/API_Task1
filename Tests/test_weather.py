import pytest
import requests
import json
import datetime as dt


class GetWeatherForeCast():

    def __init__(self):
        self.url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
        self.params = {
            'dataType': 'rhrread',
            'lang': 'en'
        }


    def current_weather_response(self, api_url, params):
        response = requests.get(url=api_url, params=params)
        #response_data = json.loads(response.text)
        #print(response_data)
        return response


class TestCase1(object):
    def test_weather_response_code(self):
        em = GetWeatherForeCast()
        #print(em.url)
        get_response = em.current_weather_response(em.url, em.params)
        assert get_response.status_code == 200

class TestCase2(object):
    def test_temprature_date(self):
        em = GetWeatherForeCast()
        get_response = em.current_weather_response(em.url, em.params)
        record_time = get_response.json()['temperature']['recordTime']
        current_date = record_time.split("T")[0] #"2020-08-05T18:45:00+08:00" to [2020-08-05, 18:45:00+08:00]
        date_from_response = dt.datetime.strptime(current_date, '%Y-%m-%d').date()
        today_date = dt.datetime.now().date() #Today date
        assert date_from_response == today_date
