import System.Environment
p 0=1
p n=n*p(n-1)
c n k=p n/(p k*p(n-k))
f n=h n 0 1
h 0 a b=a
h n a b=h(n-1)b(a+b)
w n=f(floor(logBase 2(c n (n-2)*c n (n-3)/n))+1)
main=do
 a<-getArgs
 print(w(read(head a)+1))