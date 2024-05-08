# задача 7.1
month = 15
spring_month = [3, 4, 5]
summer_month = [6, 7, 8]
winter_month = [12, 1, 2]
autmn_month = [9, 10, 11]
if month in spring_month:
    print("весна")
elif month in summer_month:
    print("лето")
elif month in winter_month:
    print("зима")
elif month in autmn_month:
    print("осень")
else: print("некорректный номер месяца")

# задача 7.2
is_logged_in = True
has_items_in_cart = True
has_shipping_address = True

if is_logged_in and has_items_in_cart and has_shipping_address:
    print("Все критерии для оформления заказа выполнены. Заказ может быть оформлен")
else: print("Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию")

total_purchase = 1100
min_purchase = 1000
is_first_order = True

if is_first_order and min_purchase and total_purchase:
    print("Вы получаете скидку!")

# задача 7.3
number = 15
happy_number = [7, 13, 21]


if number in range(1, 101):
    print("Число в указанном диапазоне")
elif number in happy_number:
    print("Счастливое число!")
else: print("Не повезло")






