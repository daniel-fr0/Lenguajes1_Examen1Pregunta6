from math import prod, log2, floor

def factorial(n):
	return prod(range(1,n+1))

def binomial(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))

def N(n,k):
	return binomial(n,k)*binomial(n,k-1)/n

def fib(n,a=0,b=1):
	if n==0:return a
	if n==1:return b
	return fib(n-1,b,a+b)

def wadefoc(n):
	return fib(floor(log2(N(n+1,n-1)))+1)


# Verifico que los resultados sean iguales
import sys
sys.argv = ["", "500"]

from hit import W
for i in range(2,501):
	if W(i+1)!=wadefoc(i):
		print("ERROR at", i, ":", W(i+1), "!=", wadefoc(i), "!!!")
		exit()
print("OK")

# Verifico tambien cuantos caracteres tiene el codigo de hit1.py
file = open("hit.py", "r")
data = file.read()
file.close()
print(len(data))

file = open("hit2.hs", "r")
data = file.read()
file.close()
print(len(data))