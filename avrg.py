# import np
import numpy as np

#/////////////////
lst = []
n = int(input("enter range ==> "))
sum = []

#////////////////
for i in range(0, n):
    ele = int(input())
    lst.append(ele)   
print(lst) 

#//////////////   
total = np.sum(lst)
print (total) 

#///////////////
avr = total / n 
print(avr) 
    
    
