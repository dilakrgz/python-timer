#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
try:
    my_time =int(input("enter the time in seconds:")) #int burada "10" formatından 10 formatına taşır
    for x in range(my_time,0,-1): #range(baslangıc,bıtıs,adım)
        seconds=x % 60
        minutes=int(x/60)%60 #bunun yerıne (x//60)%60 da yazılabilir
        hours=int(x/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)  #program 1 saniye bekler
    print("TIME'S UP!")
except ValueError:
    print("please enter a number")
   


# In[ ]:





# In[ ]:




