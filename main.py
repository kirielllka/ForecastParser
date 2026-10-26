#Сценарий (реалистичный)
# Команда аналитики хочет ежедневный отчёт по городам присутствия компании:
# температура, осадки, ветер на 7 дней вперёд + климатическая норма за прошлый год для сравнения.
# Отчёт формируется скриптом, который:
# 1Принимает список городов (из конфига).
# 2Резолвит каждый город в координаты через геокодинг.
# 3Запрашивает прогноз и историю.
# 4Собирает всё в структурированный отчёт (JSON + краткая сводка в консоль).
# 5Устойчив к сбоям: один город упал — остальные продолжаются.
# 6Не превышает rate limit.
# 7Тестируется без сети.
import asyncio

import logging

from client.GeocordingReq import GeocordingReq
from client.CityInfoForm import CityYamlInfoFormer
import yaml

from logger_config import setup_logger

setup_logger()

logger = logging.getLogger(__name__)

try:
    with open("cities.yaml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        logging.info('File was parsed successfully')
except Exception as e:
    logger.error(e)


data = []
for city in cfg['cities']:
    data.append(asyncio.run(GeocordingReq.get_geocoring(city)))
CityYamlInfoFormer.city_info_former(data)
