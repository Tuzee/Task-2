year = 0
while year != 1799:
    year = int(input("В каком году родился Пушкин? "))
if year == 1799:
    print("Верно")
    question_2 = int(input("В какой день родился Пушкин?"))
    if question_2 == 26:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год")