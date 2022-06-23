year = 0
day = 0
while year != 1799:
    year = int(input("В каком году родился Пушкин? "))
if year == 1799:
    print("Верно")
    while day != 26:
        day = int(input("В какой день родился Пушкин?"))
    if day == 26:
        print("Верно")