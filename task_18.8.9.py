number_tickets = int(input("Укажите количество билетов :"))
Price = 0
for ticket in range(number_tickets):
    age = int(input("Укажите возраст поcетителя :"))
    if age <= 18 :
        Price +=0
        print("Просмотр бесплатный")
    if 18< age <= 25:
        Price +=990
        print("Стоимость билета: 990")
    if age > 25:
        Price +=1390
        print("Стоимость билета: 1390")

if number_tickets >= 3:
        Price=Price*(100-10)/100
print("Стоимость всех билетов :",Price)
