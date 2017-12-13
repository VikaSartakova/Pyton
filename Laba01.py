import math
from math import tanh
from math import asin

a = int(input('Enter a:'))
x= int(input('Enter x:'))

G=(3*(3*a**2-13*a*x+4*x**2))/(54*a**2+87*a*x+35*x**2)

print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, G))

a = int(input('Enter a:'))
x= int(input('Enter x:'))

F=-tanh(63*a**2-5*a*x-2*x**2)

print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, F))

a = float(input('Enter a:'))
x= float(input('Enter x:'))

Y=-asin(8*a**2-15*a*x-27*x**2)

print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, Y))