
__author__ = 'Ялинскене Мария Александровна'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
n=int(input("Input any number please  "))
n1=n%10
print(n1)
while n>9:
    n = n//10
    n1=n%10
    print(n1)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a=int(input("Введите значенние А  "))
b=int(input("Введите значение В  "))
c=a+b
b=c-b
a=c-a
print(" Новое значение А = ", a , "Новое значение В= ", b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input("Сколько Вам лет?   "))
if age >=  18:
	print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
