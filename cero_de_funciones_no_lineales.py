# Codigo para hallar ceros de funciones no lineales
# Metodo de biseccion
import math
import random

def samesign(a, b):
        return a * b > 0

def f(x):
	return 3**(1/3) - x

def bis(func,ini,fin):
	assert not samesign(func(ini),func(fin))

	for i in range(54):
		mit = (ini + fin) / 2

		if not samesign(func(ini),func(mit)):
			fin = mit
		else:
			ini = mit

	return mit

arr = [1,-1]
sol = []
for i in arr:
	while 1:
		tmp = random.randint(1,100) - 4
		if samesign(i,f(tmp)):
			sol.append(tmp)
			break

sol.sort()

print(bis(f,sol[0],sol[1]))

# f(x) = 3**(1/3) - x = 0 					: 1.4422495703074083
# f(x) = 4*math.cos(x) - math.e ** x 		: 0.9047882178730177
# f(x) = x**2 - math.log(10 + x,math.e) 	: 1.5645919637620995
# f(x) = x - math.tan(x) 					: 1.5707963267948952

