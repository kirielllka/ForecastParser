import logging
import sys


def setup_logger():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #форматер для логов

    file_handler = logging.FileHandler('logging.log',mode='a')
    file_handler.setFormatter(formatter) #
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)#Обработчик для консоли (чтобы видеть, что происходит)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger()#Настройка корневого лога
    root_logger.setLevel(logging.INFO)

    if root_logger.hasHandlers():#очистка прошлых хендлеров
        root_logger.handlers.clear()

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)