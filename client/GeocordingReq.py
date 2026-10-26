import asyncio

from typing import List

import logging

import requests_async as ra

logger = logging.getLogger(__name__)

class GeocordingReq:
    request_url = 'https://geocoding-api.open-meteo.com/v1/search?'
    @classmethod
    async def get_geocoring(cls, city_name:str)->dict:

        url = f'{GeocordingReq.request_url}name={city_name}'
        try:
            response = await ra.get(url,
                              json={'key':'value'})
            logger.info('City coordinate was parsed')
            return {'status': response.status_code,
                    'data': response.json()['results'][0]}

        except Exception as e:
            logger.error(f'City coordinate was not parsed {e}')


