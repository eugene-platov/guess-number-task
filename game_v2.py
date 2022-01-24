"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import typing


GUESSED_NUMBER_RANGE = [1, 101]


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(*GUESSED_NUMBER_RANGE) # предполагаемое число
        if number == predict_number:
            break # выход из цикла если угадали

    return count

def binary_search(number: int = 1) -> int:
    """Ищем число используя бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min, max = GUESSED_NUMBER_RANGE[0], GUESSED_NUMBER_RANGE[1]

    while True:
        count += 1
        predict_number = (min + max) // 2

        if predict_number == number:
            break

        if predict_number > number:
            max = predict_number - 1
        else:
            min = predict_number + 1

    return count


def score_game(random_predict: typing.Callable[[int], int]) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (Callable[[int], int]): функция угадывания, должна возвращать целое число

    Returns:
        int: среднее количество попыток
    """
    count_ls: list[int] = []
    # np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(*GUESSED_NUMBER_RANGE, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score