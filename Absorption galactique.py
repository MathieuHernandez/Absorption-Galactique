from math import *

def integrate(f,a,b,n):
    t=(b-a)/n
    sum=0
    for i in range(n):
        sum+=f(a+t*i)*t
    return sum
def g(x,y,z):
    return x+y**2+z**3

def dInt(g,a,b,c,d,e,f,n):
    t1=(b-a)/n
    t2=(d-c)/n
    t3=(f-e)/n
    sum=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum+=g(a+t1*i,c+t2*j,e+t3*k)*t1*t2*t3
    return sum
