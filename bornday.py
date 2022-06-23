question = int(input("В каком году родился Пушкин?"))
if question == 1799:
    question_2 = int(input("В какой день родился Пушкин?"))
    if question_2 == 26:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год")