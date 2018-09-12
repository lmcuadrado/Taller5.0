import numpy as np
from scipy.linalg import expm, sinm, cosm
#import matplotlib.pylab as plt

#------Punto 1--------

#------Punto 2--------
H=np.array([[0.0,0.0,0.0,0.0],[0.0,-2.0,1.0,0.0],[0.0,1.0,-2.0,0.0],[0.0,0.0,0.0,-4.0]])

print H

#------Punto 3--------
T=1.0
N=100000.0
t=T/N

U=expm(-(1j)*t*H)

#print U
#------Punto 4--------
a=(1.0/np.sqrt(2))
b=np.array([0,1,1,0])
x=a*b

print x

#------Punto 5--------
UN= np.linalg.matrix_power(U,100000)

x0= np.linalg.solve(UN,x)
print x0

#------Punto 5--------

c=np.matmul(UN,x0)
print c

