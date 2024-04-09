Вариант 1
money=int(input("Введите сумму вклада:"))
per_cent= { 'TKB' : 5.6, 'SKB':5.9 , 'VTB' : 4.28 , 'SBER' : 4.0 }
TKB= int((per_cent['TKB']) * (money/100))
SKB= int((per_cent['SKB']) * (money/100))
VTB= int((per_cent['VTB']) * (money/100))
SBER= int((per_cent['SBER']) * (money/100))
deposit =[TKB,SKB,VTB,SBER]
print("Накопленные средства за год в разных банках:" ,', '.join(map(str, deposit)))
print("Максимальное накопление за год :", max(deposit))

Вариант 2
money =int(input("Введите сумму вклада:"))
per_cent = { 'TKB' : 5.6, 'СКБ':5.9 , 'ВТБ' : 4.28 , 'СБЕР' : 4.0 }
deposit =[]
deposit.append(int((per_cent['TKB']) * (money/100)))
deposit.append(int((per_cent['SKB']) * (money/100)))
deposit.append(int((per_cent['VTB']) * (money/100)))
deposit.append(int((per_cent['SBER']) * (money/100)))
print("Накопленные средства за год в разных банках:" ,', '.join(map(str, deposit)))
print("Максимальное накопление за год :", max(deposit))
