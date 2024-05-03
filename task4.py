list_players = ["Маша","Петя", "Саша", "Оля", "Кирилл"]
last_players = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_players)
print("Первый участник:", reestr["Первый участник"])

list_participants = ["Орлов", "Петров", "Иванов",
"Сидоров", "Васильев", "Черепахин"]
last_participant = list_participants[-1]
winner = {"Первый лыжник": list_participants[0]}
print("Последний лыжник:", last_participant)
print("Первый лыжник:", winner["Первый лыжник"])

sps_book = ["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон", "Ревизор", "Гранатовый браслет"]
last_book = sps_book[-1]
book = {"Первая книга": sps_book[0]}
print("Последняя книга:", last_book)
print("Первая книга:", book["Первая книга"])

shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник", "Рюкзак", "Термос", "Миска", "Ветровка", "Коврик"]
unique_items = set(shopping_list)
len(unique_items)
print("Количество уникальных товаров:", len(unique_items))

seasons_dict =  {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
print(seasons_dict)


