import System.Environment
p 0=1
p n=n*p(n-1)
c n k=p n/(p k*p(n-k))
f 0=0
f 1=1
f n=f(n-1)+f(n-2)
n x y=c x y/c x (y-1)/x
l=logBase 2
w x=f(truncate(l(n (x+1)(x-1)))+1)
main::IO()
main=do
 a<-getArgs
 print $ w $ read $ head a