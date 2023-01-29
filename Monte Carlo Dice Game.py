#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import random
z=int(input("Your bet money"))
count=int(input("The money you have in hand"))
sim=int(input("No: of simulations:"))

end_balance=[]
prob=[]
def win():
    a=random.randint(1,6)
    b=random.randint(1,6)
    if(a==b):
     return True
    else:
     return False
plt.title("Monte carlo sims")
plt.xlabel("Nuber of rolls")
plt.ylabel("Money left")
plt.xlim([0,count])
for i in range(sim):
    num_roll=[0]
    num_win=0
    balance=[1000]
    while(num_roll[-1]<=count):
     o=win()
     if o:
        balance.append(balance[-1] + 4*z)
        num_win+=1
     else:
        balance.append(balance[-1] -z)
     num_roll.append(num_roll[-1]+1)
    end_balance.append(balance[-1])
    prob.append(num_win/num_roll[-1])
    plt.plot(num_roll,balance)
plt.show()    
r=sum(end_balance)/len(end_balance)
w=sum(prob)/len(prob)
print("avg balance: $"+str(r))        
print("avg win:"+str(w))    
if(w*100<=50):
    print("Game is not fair, you'll most likely lose")
 

