# import np
import numpy as np

#/////////////////
lst = []
n = int(input("enter reang ==> "))
sum = []

#////////////////
for i in range(0, n):
    ele = int(input())
    lst.append(ele)   
print(lst) 

#//////////////   
touta = np.sum(lst)
print (touta) 

#///////////////
avr = touta / n 
print(avr) 
    
    