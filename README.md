# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/eugene-platov/guess-number-task#описание-проекта)

[2. Какой кейс решаем?](https://github.com/eugene-platov/guess-number-task#какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/eugene-platov/guess-number-task#краткая-информация-о-данных)

[4. Результаты](https://github.com/eugene-platov/guess-number-task#результаты)

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](https://github.com/eugene-platov/guess-number-task#оглавление)


### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток, при этом обеспечивая воспроизводимость

**Условия соревнования:**
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**
Учимся писать хороший код на python

### Краткая информация о данных
Компьютер всегда загадывает числа от 1 до 100

:arrow_up: [к оглавлению](https://github.com/eugene-platov/guess-number-task#оглавление)

### Результаты:
Бинарный поиск в качестве алгоритма угадывания обеспечивает стабильный поиск загаданного числа от 1 до 100 максимум с 7 попытки

:arrow_up: [к оглавлению](https://github.com/eugene-platov/guess-number-task#оглавление)