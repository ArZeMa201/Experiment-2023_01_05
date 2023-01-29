import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Import document#
url = 'https://raw.githubusercontent.com/ArZeMa201/Experiment-2023_01_05/main/Data17012023%20-Lambda.txt'
df = pd.read_csv(url, delimiter = "\t")


#slicing 
i = df.index
index = df['Timestamp']== '16:24:07.28555'
result = i[index]
print(result)


#create figure 
fig, ax1 = plt.subplots()
fig.set_size_inches(20, 11)

# #Plot complete lambda3 
ax1.plot(df['Timestamp'],df['Lambda3'])

plt.xticks(np.arange(1,2064, step=25), size='small')                            # ax.xaxis.set_major_locator(ticker.MultipleLocator(25))

plt.grid(True, linewidth = "0.4")
plt.xticks(rotation=45)
ax1.set_ylabel('Lambda3')
ax1.set_xlabel('Time')

plt.grid(True)
plt.show()