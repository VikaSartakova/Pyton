from math import asin
from math import tanh

c = input('Если хотите вычислить значение G нажмите 1, введите 2 для вычисления F, введите 3 для вычисления Y')


if c == '1':
    a = int(input('Enter a:'))
    x = int(input('Enter x:'))
    b = 54*a**2+87*a*x+35*x**2
    if b != 0:
        G=(3*(3*a**2-13*a*x+4*x**2))/b
        print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, G))
    else: print('Введите другие значения x и a')
elif c == '2':
      a = int(input('Enter a:'))
      x = int(input('Enter x:'))
      F = -tanh(63 * a ** 2 - 5 * a * x - 2 * x ** 2)
      print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, F))
elif c == '3':
    a = float(input('Enter a:'))
    x = float(input('Enter x:'))
    d = 8*a**2-15*a*x-27*x**2
    if d >= 0:
        Y = -asin(d)
        print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, Y))
    else:  print('Введите другие значения x и a')

else: print("Вы ввели не корректное значение")
