# Python-Tasks
Задания по "Основам изучения Python"

17.7.3:   дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом, что ключ — название банка, значение — процент. Напишите программу, в результате которой будет сформирован список deposit значений — накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.
per_cent = { 'ТКБ' : 5,6 , 'СКБ' : 5,9 , 'ВТБ' : 4,28 , 'СБЕР' : 4,0 }
Добавьте в программу поиск максимального значения и его вывод на экран в формате:
Максимальная сумма, которую вы можете заработать — депозит [i], где вместо deposit[i] будет выведено максимальное значение списка.

Задание 18.8.19:
Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:
1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
От 18 до 25 лет — 990 руб.
От 25 лет — полная стоимость 1390 руб.
3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
