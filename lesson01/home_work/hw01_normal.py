
__author__ = 'Ялинскене Мария Александровна'

n=int(input("Input any number please  "))
n1=n%10 #последняя цифра числа
while n>9:
    n = n//10
    n2=n%10 # следующая цифра числа
    if n2>n1:
        n1=n2
print(n1)


# Задача-2: Здесь совершенно не уверена 
a=int(input("Введите значенние А  "))
b=int(input("Введите значение В  "))
tulp1=(a,b)
a=tulp1[1]
b=tulp1[0]
print(" Новое значение А = ", a , "Новое значение В= ", b)


# Задача-3:

a=int(input("Введите значенние а "))
b=int(input("Введите значение в "))
c=int(input("Введите значение с  "))
import math
d=math.sqrt((b**2)-(4*a*c))
if d <0:
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print("Корни равны ",x1,x2)
elif d=0:
    x1=(-b+d)/(2*a)
    print("Корень равен ",x1)
else:
    print ("Корней не существует")
