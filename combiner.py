import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

xmin=-2
xmax=0.5
ymin=-1
ymax=1

dragon=[]

for index in range(1,19):
   print(index, " is loading")
   name="data"+str(index)
   with open(name,'rb') as rb:##CHANGE THIS TO YOUR INDEX
        load=pickle.load(rb)
        dragon.extend(load)
   print(index, " is loaded")
   if index ==16:
      print("Prepare for SWAPPPPPPPP")
        


print("start print")


fig,ax = plt.subplots()

ax.imshow(dragon,extent=[xmin,xmax,ymin,ymax], interpolation="bicubic")
plt.savefig("combines.png",dpi=3000)
plt.show()

print('saved')
