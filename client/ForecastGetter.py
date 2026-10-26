import logging

import requests_async as ra

class ForecastGetter:
    request_url_start = 'https://api.open-meteo.com/v1/forecast?'
    request_url_end = ('&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,visibility,'
                         'rain,weather_code&models=dwd_icon_seamless&forecast_days=7')

    @staticmethod()
    def forecast_get(city_data:dict)->dict:
        url = (f'{ForecastGetter.request_url_start}latitude={city_data['Latitude']}'
               f'&longitude={city_data['Longitude']}{ForecastGetter.request_url_end}')
        try:
            response = ra.get(url, json={'key':'value'})
            return {'status':response.status_code,'data':response.json()['results']}
        except Exception as e:
            return {'status':response.status_code,'data':{e}}
