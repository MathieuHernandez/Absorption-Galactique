
##### MODULES
from math import *
import numpy as np



#### CONSTANTES
rho0=1098
hd=0.1344
hr=2.26
cb=0.0641
rm=6.71
rb=2.07
rc1=3
rc2=13
r0=2.3
Rs=8
Zs=0.0155
    



##### FONCTIONS
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
    
    
def rhoDisque(r,z,rho0,hr,hd):
    return rho0*np.exp(-r/hr)/(np.cosh(z/hd)**2)
    
def formeBras(theta,r0,theta0,k):
    return r0*np.exp(k*(theta-theta0))

def DistanceMin1bras(r,theta,r0,theta0,k,rc1,rc2):
    dmin=0.
    theta1=0.
    theta2=0.
    thetabras=0.
    rm=0.
    dmin=1e10
    theta1=1./k*np.log(rc1/r0)+theta0
    theta2=1./k*np.log(rc2/r0)+theta0
    thetabras=theta
    while thetabras>theta1:
        theta=theta-2*np.pi
    while thetabras<theta1:
        theta=theta+2*np.pi
    while thetabras<theta2:
        rm=formeBras(thetabras,r0,theta0,k)
        if np.abs(rm-r)<dmin:
            dmin=abs(rm-r)
        theta=thetabras+2*np.pi
    return dmin

def DistanceMin4Bras(r,theta,z,r0,theta0,k,rc1,rc2):
    dmin=0.
    i=0
    dmin=1e10
    for i in range(0,4):
        d=DistanceMin1bras(x,y,r0,theta0-(i*np.pi/2),k,rc1,rc2)
        if d<dmin:
            dmin=d
    return (dmin**2+z**2)**0.5
    
def RhoBrasSpiraux(r,theta,r0,theta0,k,rhob,rm,cb,rb,hb,rc1,rc2):
    dmin=0.
    gb=0.
    wb=0.
    dmin=DistanceMin4Bras(r,theta,z,r0,theta0,k,rc1,rc2)
    if r<=rm:
        gb=1
    else:
        gb=np.exp(-(r-rm)**2/(rb**2))
    wb=cb*r
    return rhob*gb*np.exp(-(dmin/wb)**2)*np.exp(-(z/hb**2))
    
def rhoGalaxi(r,theta,z,r0,theta0,k,rm,rb,hb,rho0,hr,hd,rci,rc2):
    return rhoDisque+RhoBrasSpiraux
        
##### PROGRAMME
        
        
##### GRAPHIQUES
    
