import math,sys
C=math.comb
F=lambda n,a=0,b=1:n<1 and a or F(n-1,b,a+b)
W=lambda n:F((C(n,n-2)*C(n,n-3)//n).bit_length())
print(W(int(sys.argv[1])+1))