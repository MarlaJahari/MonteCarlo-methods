#!/usr/bin/env python
# coding: utf-8

# In[63]:


#monte carlo monty hall problem
#from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
import numpy as np
import random as rd
 
n=int(input("No: of simulations:"))
doors=np.array([1,0,0])
swp=[]
stp=[]
b=rd.randint(0,2)
def monte(n):
 count1=0
 count2=0
 for i in range(n): 
  shuffle(doors)
  b=rd.randint(0,2)
  if(doors[b]==1):
   count1+=1
  else:
   count2+=1  
  stp.append(count1/(i+1))
  swp.append(count2/(i+1))
 return count1,count2
monte(n)
print("Probability of winning if you stick to your choice: "+str(stp[-1]*100)+" %")
print("Probability of winning if you switch your choice: "+str(swp[-1]*100)+" %")
plt.xlabel("No: of simulations")
plt.ylabel("Probability")
plt.plot(swp,label="For switching")
plt.plot(stp,label="For sticking")
plt.legend(loc='best')
plt.title("Monte Carlo Monty Hall")
plt.grid()
plt.show()
if(stp[-1]<swp[-1]):
 plt.title("Congratulations you win a")
 im=mpimg.imread(r"C:\Users\giggl\OneDrive\Pictures\cool-goat.png")  
 plt.imshow(im)  
 plt.axis('off')
 plt.show()


# In[ ]:




