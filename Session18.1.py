# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:51:30 2018

"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy as s
import matplotlib.pyplot as plt
import math
Mean_p=100
Std_p =15

print("Mean,standard deviation  of population :","\nMean:",Mean_p,"\nStandard deviation:",Std_p)
N=36
Mean_s=108
Std_s = Std_p/ math.sqrt(N)

print("Mean,standard deviation  of sample with N:",N,"\nMean:",Mean_s,"\nStandard deviation:",Std_s)
Z= (Mean_s-Mean_p)/Std_s
print("\nZ-score :",Z)

print("""From the stated hypothesis,
      we know that we are dealing with a 2-tailed hypothesis test. Unless otherwise stated,
      we can assume an alpha level of 0.05. This gives us a critical Z score of: 3.25""")
P_value = s.special.ndtr(Z)

print("""You can look at the probability by looking at z- table and 
      p-value associated with 3.20 is 0.9993 i.e. probability of having value less than 108 is 0.9993 and 
      more than or equals to 108 is (1-0.9993)=0.0007.""")

plt.figure(figsize=(10,8))

plt.fill_between(x=np.arange(-4,-3.25,0.01), 
                 y1= stats.norm.pdf(np.arange(-4,-3.25,0.01)) ,
                 facecolor='red',
                 alpha=0.35)

plt.fill_between(x=np.arange(-3.25,3.25,0.01), 
                 y1= stats.norm.pdf(np.arange(-3.25,3.25,0.01)) ,
                 facecolor='Orange',
                 alpha=0.35)

plt.fill_between(x=np.arange(3.25,4,0.01), 
                 y1= stats.norm.pdf(np.arange(3.25,4,0.01)) ,
                 facecolor='red',
                 alpha=0.5)


plt.text(x=-1.8, y=0.15, s= "Null Hypothesis:"+ str(P_value))
plt.text(x=3.7, y=0.01, s= "3.25")
plt.text(x=-3.7, y=0.01, s= "-3.25")

print("It is less than 0.05 so we will reject the Null hypothesis i.e. there is raw cornstarch effect.")


