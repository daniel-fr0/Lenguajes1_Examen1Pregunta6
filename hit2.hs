import System.Environment
p 0=1
p n=n*p(n-1)
c n k=p n/(p k*p(n-k))
f n=h n 0 1
h 0 a b=a
h n a b=h(n-1)b(a+b)
n x y=c x y*c x (y-1)/x
l=logBase 2
w x=f(truncate(l(n(x+1)(x-1)))+1)
main=do
 args<-getArgs
 print(w(read(head args)))