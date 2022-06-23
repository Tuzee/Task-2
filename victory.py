summary_questions = 0
right_answers = 0
mistakes = 0
while True:
    #Первый персонаж
    person1 = int(input("В какой день родился наруто? "))
    if person1 == 20:
        right_answers += 1
    else:
        mistakes += 1
    summary_questions += 1
    #Второй персонаж
    person2 = int(input("В какой день родился Саске? "))
    if person2 == 23:
        right_answers += 1
    else:
        mistakes += 1
    summary_questions += 1
    #Третий персонаж
    person3 = int(input("В какой день родилась Сакура? "))
    if person3 == 28:
        right_answers += 1
    else:
        mistakes += 1
    summary_questions += 1
    #Четвертый персонаж
    person4 = int(input("В какой день родился Какаши? "))
    if person4 == 15:
        right_answers += 1
    else:
        mistakes += 1
    summary_questions += 1
    #Пятый персонаж
    person5 = int(input("В какой день родился Ямато? "))
    if person5 == 10:
        right_answers += 1
    else:
        mistakes += 1
    summary_questions += 1
    #Подсчет процентов
    procent_right_anwsers = right_answers * 100 / summary_questions
    procent_mistake_answers = mistakes * 100 / summary_questions

    print("Количество правильных ответов: ", right_answers)
    print("Количество ошибок : ", mistakes)
    print("Процент правильных ответов: ", procent_right_anwsers, "%")
    print("Процент ошибок: ", procent_mistake_answers, "%")

    again = int(input("Вы хотите начать сначала? Введите 1 если да. Введите 2 -если нет "))
    if again == 2:
        break