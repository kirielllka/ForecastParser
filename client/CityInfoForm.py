import sys
from typing import List

import yaml

import logging

logger = logging.getLogger(__name__)


class CityYamlInfoFormer:
    @staticmethod
    def city_info_former(data: List[dict]) -> None:
        result = {'cities':[]}
        logger.info(f'City data: {data}')
        for city in data:
            form_data = {
                'CityName': city['data']['name'].replace('’', ''),
                'Latitude': city['data']['latitude'],
                'Longitude': city['data']['longitude'],
                'Country': city['data']['country'],
                'TimeZone': city['data']['timezone'],
            }
            result['cities'].append(form_data)
        logger.info('City info formated')
        with open('former_city.yaml', 'w') as f:
            yaml.dump(result, f, default_flow_style=False)
            logger.info('City_info file was written')

