dayNumber = int(input("введите число: "))#День недели в виде числа
result = dayNumber >= 1 and dayNumber <= 7

if result == False:
    print("Не правильный день недели. Программа закрывается...")
    exit()

dayOfWeek = "none"

if dayNumber == 1:
    dayOfWeek = "Понедельник"
elif dayNumber == 2:
    dayOfWeek = "вторник"
elif dayNumber == 3:
    dayOfWeek = "средат"
elif dayNumber == 4:
    dayOfWeek = "четверг"
elif dayNumber == 5:
    dayOfWeek = "пятница"
elif dayNumber == 6:
    dayOfWeek = "суббота"
elif dayNumber == 7:
    dayOfWeek = "воскресенье"  

print(dayOfWeek)
