def validate_amount_of_water(amount_of_water: float) -> bool:
    """
    Функция валидатор значения количества воды, которое введёт пользователь.
    Если значение не в пределах от 0.0 до 1.0 - возвращается False. Иначе True
    :param amount_of_water: (float) количество воды введёное пользователем.
    :return: (bool). True в случае прохода валидации, иначе False.
    """
    if amount_of_water < 0.0 or amount_of_water > 1.0:
        return False
    return True
