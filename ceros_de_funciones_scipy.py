# Codigo para hallar ceros de funciones no lineales
# Metodo de biseccion y Metodo de Newton
def f(x):
	return 3**(1/3) - x

import scipy.optimize
import math

print(scipy.optimize.bisect(f, 1, 10))  #1.4422495703071263
print(scipy.optimize.newton(f, 3))      #1.4422495703074083

def f1(x):
	return 4*math.cos(x) - math.e ** x

print(scipy.optimize.bisect(f1, 0, 10))  #0.904788217873147
print(scipy.optimize.newton(f1, 10))      #0.9047882178730218

def f2(x):
	return x**2 - math.log(10 + x,math.e)

print(scipy.optimize.bisect(f2, 0, 10))  #1.564591963762041
print(scipy.optimize.newton(f2, 10))      #1.564591963762099

def f3(x):
	return x - math.tan(x)

print(scipy.optimize.bisect(f3, 1, 10))  #1.5707963267958576
#print(scipy.optimize.newton(f3, 3))      #no converge
