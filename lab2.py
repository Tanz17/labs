import math


def task1():
     x = int(input('Введите значение - x: '))

     result = 0

     if x <= 3:
          result = -1 * x**2 + 3*x + 9
     else:
          result = x / (x**2 + 1)
     return result


def findIsosceles():
     A = []
     a = input("Введите 3 значения стороны, разделяя их пробелами: ")

     for i in a.split(' '):
          A.append(int(i))
     for i in range(2):
          if A[i] == A[i+1] and A[i+1] == A[i+2]:
               return ('Не равнобедренный')
          if A[i] == A[i+1] or A[i] == A[i+2] or A[i+1] == A[i+2]:
               return ("Равнобедренный")
          else:
               return ('Не равнобедренный')
          
def convertorDegToRad():
     option = int(input('Введите значение: 1 - Радианы в Градусы / 0 - Градусы в Радианы\n'))
     value = int(input('Введите значение величины:\n'))

     match option:
          case 0:
               return value * 0.017
          case 1:
               return value * 57.3
          case _:
               return f'Опции под названием: {option} не существует'


print(convertorDegToRad())
