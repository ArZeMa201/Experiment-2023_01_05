import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

#Import document
url = 'https://raw.githubusercontent.com/ArZeMa201/Experiment-2023_01_05/main/Data17012023_Lambda.txt'
df = pd.read_csv(url,index_col=0, delimiter = "\t", parse_dates=(True))



#resample
df_n = pd.DataFrame(df.resample('S').agg({'Lambda3':'mean','Lambda4':'mean','Lambda5':'mean',
                                          'Lambda6':'mean','Lambda7':'mean','Lambda9':'mean',
                                          'Lambda10':'mean','Lambda11':'mean','Lambda12':'mean'}))
Reps = df_n.between_time('16:24:02', '16:35:45')                                 #total time of the 15 iterations 

#Variables

LI= []

LD={}       #Lambda changes dictionary

LE_6 ={}    #Lambda arrenged for events dictionary
MeanL6 =[]
index = []
 
i = 0

#initial lambda values
for x in Reps['Lambda6']: 
    if x <= 1534.40:
        LI.append(x)
    else:
        i+=1
        break

MeanL = statistics.fmean(LI)

LIpm = MeanL*1000                       #Initial lambda in picometers


for j in Reps['Lambda6']:               #save the values of lambdaX changes for the given values
    key = 'Event%s'%i
    if j >= 1534.40:
        LD.setdefault(key,[]).append(j)
    else:
        i+=1    
     
for y in range(len(LD.keys())):         #Lambda arrenged for events dictionary 
    key = 'Event%s'%y
    LE_6.setdefault(key,(list(LD.values())[y]))
    
#remove unnecesarry events
for y in range(len(LE_6.keys())):
    f = len(LE_6['Event%s'%y])
    if f <= 2:
        del LE_6['Event%s'%y]   
    else: 
        MeanL6.append(statistics.fmean(LE_6['Event%s'%y]))                         #Mean value    
        index.append('Event%s'%y) 
                                                                                 
#Lambda6 values in picometers   
# L6 = [x *1000 for x in MeanL6]

#delta lambda 6 Picometers
DL6 = [z - MeanL for z in MeanL6]
#Curvature X theretical value of 0.85
K = [v/((w*(1-0.000078))*0.85) for v,w in zip(DL6,MeanL6)]

#standard deviation of kurvature
SDK6 = [np.std(K)]

fig,ax1 = plt.subplots()

ax1.plot(DL6,K, marker='X', color='black')
  
plt.title('Lambda6', loc=('center'))
plt.grid(True,)

ax1.set_ylabel('Curvature (1/mm)')
ax1.set_xlabel('Wavelength Shift (nm)')
plt.grid(True)
plt.show()

#strain 
# E = np.array(DL6)/np.array(L6)



#Lambda6 Dataframe arranged per event
# Lambda6 = pd.DataFrame(PM,index)



                                               
