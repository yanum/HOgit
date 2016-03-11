# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

d=range(10)
suma=0
for i in d:
    if (i%3==0 or i%5==0):
        suma=suma+i
        print(i)
print(suma)

# <codecell>

d=range(1000)
suma=0
for i in d:
    if (i%3==0 or i%5==0):
        suma=suma+i
print(suma)

# <codecell>

num=13195
rangenum=range(13195)
v=[0]
for i in rangenum:
    if (i>0 and num%i==0):
        v.extend([i])
for j in v:
    if j > 2: 
        x=range(2,i) #si es menos que 2 no es primo, por lo tanto devolverá Falso
        for j in x:  #un rango desde el dos hasta el numero que nosotros elijamos

# <codecell>

print(v)

# <codecell>

from math import sqrt
num=13195
rangenum=range(num)
v=[0]
for i in rangenum:
    if (i>0 and num%i==0):
        v.extend([i])
v

# <codecell>

v

# <codecell>

z=[0]
for i in v:
     if es_primo(i):
        z.extend([i])

max(z)

# <codecell>


def es_primo(num):
  if num < 2:     
    return 
  for i in range(2, num): 
     if num % i == 0:    
         return 
  return True

print es_primo(3)    

# <codecell>

X = [7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06]

Y= [28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89]

# <codecell>


import matplotlib.pyplot as plt


plt.plot( X,Y, 'ro')

# or plot with: plot_url = py.plot(data, filename='basic-line')

# <codecell>


