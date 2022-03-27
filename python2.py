print ("I can add up the numbers and compare with yours")
a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите ваш ответ: "))
sum = a + b 
if c == sum:
    print ("Correctly")
elif c != sum:
    print ("неверно")