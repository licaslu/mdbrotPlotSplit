import matplotlib.pyplot as plt
import numpy as np
from cmath import *
import time
import pickle

##Predefined Values?
sqrtoneneg=sqrt(-1)


start = time.time()
print("Started")


def iterate(c,max_iter=500):
    z = c
    for n in range(max_iter):
        if abs(z) >= 2:
            return n
        z =z*z + c
    return 0


vals=[]

def create_mand(num_vals,min_x,max_x,min_y,max_y):

    dx=(max_x-min_x)/num_vals
    dy=(max_y-min_y)/num_vals
    a=min_x
    b=min_y

    vals=[]

    for q in range(num_vals): #Equivalent to Meshgrid
        row=[]
        for p in range(num_vals):
            a = min_x +p*dx
            b = min_y +q*dy
            row.append(iterate(a+b*sqrtoneneg))
        vals.append(row)
        print(q*100/num_vals,"%",q)
    return vals


#####################################Parameters###################################
num_vals=5000 #Equivalent to Linspace or Arange
xmin=-2
xmax=0.5
blockymin=-1
blockymax=1

totalLength=abs(blockymax-blockymin)

nodes=18; #Total Number of Computers Running

sectionalPer=totalLength/nodes; 
index=6; ##CHANGE THIS TO YOUR NUMBER (1-17)


ymax=sectionalPer*index+blockymin
ymin=sectionalPer*(index-1)+blockymin
vals = create_mand(num_vals,xmin,xmax,ymin,ymax)
################################################################################


#####################################Pickle#######################################
with open('./dump','wb') as wb:
    pickle.dump(vals,wb)
################################################################################
#####################################Plotting#####################################
fig,ax = plt.subplots()
ax.imshow(vals,extent=[xmin,xmax,ymin,ymax], interpolation="bicubic")
################################################################################

end=time.time()
print(end-start)

name="data"+str(index)

with open(name,'wb') as wb:##CHANGE THIS TO YOUR INDEX
    pickle.dump(vals,wb)
    

with open(name,'rb') as rb:##CHANGE THIS TO YOUR INDEX
    load=pickle.load(rb)

print(load)

plt.show()
fig.set_size_inches(100,80)
fig.savefig('one.png') ##CHANGE THIS TO YOUR INDEX


