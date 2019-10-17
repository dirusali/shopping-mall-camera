import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from random import randrange
from numpy import cumsum
from time import sleep
%matplotlib inline

people = np.random.randint(0,60, size=4)
people = sorted(people, reverse=False)
matrices = [np.zeros((10,10))] * 60

def random_vel(): 
    vel = np.random.normal(1.4, 0.2, 100)
    noise = np.random.normal(0, 0.05, 100)
    v = vel + noise
    np.random.shuffle(v)
    vf = v[0]
    dy = np.random.randint(10, size=(2))
    dist = dy[1] - dy[0]
    m = dist/10
    vx = np.sqrt(vf**2/(1+m**2))
    vy = vx*m             
    return (vf,vx,vy,dy[0],dy[1])
  
def movi():
    square = np.zeros((10,10))
    for p in people:
        r1=random.randint(1, 2)
        print(r1)
        if r1 == 1:
            vx = random_vel()[1]
            vy = random_vel()[2]
            y  = random_vel()[3]
            x = -1
            p = p -1
            while x < 10 and y < 10:
                try:
                    p += 1
                    x += vx
                    y += vy
                    print(p)
                    print(x,y)
                    square[int(y),int(x)]=1
                    matrices[p] = matrices[p] + square
                    square[int(y),int(x)]=0
                    print(matrices[p])
                except:
                    print(x,y)
                    pass
        else:
            vx = random_vel()[1]
            vy = random_vel()[2]
            y = random_vel()[3]
            x = 11
            p = p -1
            while x >=0 and y < 10:
                try:
                    p += 1 
                    x += (-vx)
                    y += vy
                    print(p)
                    square[int(y),int(x)]=1
                    matrices[p] = matrices[p] + square
                    square[int(y),int(x)]=0
                    print(matrices[p])
                except:
                    print(x,y)
                    pass
    return matrices  
    
