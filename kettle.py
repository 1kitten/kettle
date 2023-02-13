import logging.config
import time
from datetime import datetime
from threading import Thread
from database import log_into_data_base
from logger_config import dict_config
from validators import validate_amount_of_water


class Kettle(Thread):
    """
    Kettle (чайник) - класс потока. Нужен для инициализации объекта чайника.
    При инициализации есть возможность задать имя, по умолчанию Vitek VT-1155.
    """
    def __init__(self, amount_of_water: float, name: str = 'Vitek VT-1155'):
        """
        Инициализация объекта чайника.
        :param amount_of_water: (float) количество воды в чайнике.
        :param name: (str) имя чайника, по умолчанию Vitek VT-1155.
        """
        super().__init__()
        self.name: str = name
        self.is_working: bool = False
        self.amount_of_water: float = amount_of_water
        self.degrees: int = 0

    def run(self) -> None:
        """
        Данный метод вызывается при старте потока "*.start()".
        При вызове этого метода, чайник включается. Пока чайник работает,
        он кипятит воду на протяжении 10 секунд, попутно информируя пользователя об этом.
        После того, как чайник вскипятит воду - он будет выключен.
        :return:
        """
        self.is_working = True

        logger.info(f'Чайник {self.name} включился.')
        print(f'Чайник {self.name} включен.')
        log_into_data_base(
            date=datetime.now(),
            message=f'Чайник {self.name} включился'
        )

        while self.is_working:
            self.degrees += 10

            print(f'Чайник {self.name} вскипел на {self.degrees}C°')
            logger.info(f'Чайник {self.name} вскипел на {self.degrees}C°')

            if self.degrees == 100:
                self.is_working = False
            time.sleep(1)

        print(f'Чайник {self.name} выключен.')
        logger.info(f'Чайник {self.name} выключен.')

        log_into_data_base(
            date=datetime.now(),
            message=f'Чайник {self.name} выключен.'
        )


if __name__ == '__main__':
    logger = logging.getLogger('kettle_logger')
    logging.config.dictConfig(dict_config)

    amount_of_water = float(input('Введите количество воды (от 0.0 до 1.0): '))
    while not validate_amount_of_water(amount_of_water):
        print('Вы ввели неправильное количество воды! Необходимо ввести значение от 0.0 до 1.0')
        amount_of_water = float(input('Введите количество воды (от 0.0 до 1.0): '))

    user_kettle = Kettle(amount_of_water=amount_of_water)

    try:
        print('Для остановки чайника нажмите сочетание клавиш Ctrl+C')
        user_kettle.daemon = True
        user_kettle.start()
        while True:
            time.sleep(1)
            if not user_kettle.is_alive():
                exit(0)
    except KeyboardInterrupt:
        print(f'Чайник {user_kettle.name} был принудительно остановлен.')
        logger.info(f'Чайник {user_kettle.name} был остановлен')
        exit(0)
