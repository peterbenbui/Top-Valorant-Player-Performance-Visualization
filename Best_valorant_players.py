import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


valorant_data = ('/Users/peter/Downloads/valorant data.xlsx')
df = pd.read_excel(valorant_data)
df.dropna()
print(df)

viz_data = df.describe()
print(viz_data)
print('-----------------')
print("Variance")
viz_data = df[['ACS','K:D','KAST','FKPR','HS%']].var()
print(viz_data)



fig = plt.figure(facecolor = 'pink')
fig2 = plt.figure(facecolor = 'plum')
fig3 = plt.figure(facecolor = 'palegreen')
fig4 = plt.figure(facecolor = 'peachpuff')
ax = fig.add_subplot(1,1,1, projection ='3d')
ax2 = fig2.add_subplot(1,1,1)
ax3 = fig3.add_subplot(1,1,1, projection = '3d')
ax4 = fig4.add_subplot(1,1,1, projection = '3d')
xaxis = np.arange(1,500)

plt.grid()

#Line Graph First kills per round
ax.set_facecolor('pink')
ax.set_title('First Kills')
ax.set_xticks([1,250,500])
ax.set_xticklabels(['1','250','500'])
ax.set_xlabel('Ranks')
ax.set_ylabel('First Kills Per Round')
ax.set_zlabel('First Kills Per Round')

# the plot help show how first kill per round doesnt nessisarily correlate how good you are.
ax.plot(xaxis, df['FKPR'],df['FKPR'],color= 'crimson', linestyle = 'solid', marker = 'o',markersize = 1.5 ,label = 'FKPR', linewidth = 1)
ax.legend()

#Histogram Head shot precentage
ax2.set_facecolor('plum')
ax2.set_title('HeadShot')
ax2.set_xticks([.15,.20,.25,.30,.35,.40])
ax2.set_xticklabels(['15%','20%','25%','30%','35%','40%'])
ax2.set_xlabel('Head shot precentage')
ax2.set_ylabel('Player Amount')

#helps you visualize the general headshot precentage of experts
ax2.hist(df['HS%'], bins = 11, color = 'purple', label = 'HS%')
ax2.legend()

#Kills Per Death Bar Graph
ax3.set_facecolor('palegreen')
ax3.set_title('Kills Per Death')
ax3.set_xlabel('Ranks')
ax3.set_ylabel('Kills Per Death Ratio')
ax3.set_zlabel('Kills Per Death Ratio')
ax3.set_yticks([.5,1.0,1.5,2.0])
ax3.set_zticks([.5,1.0,1.5,2.0])
ax3.set_zticklabels(['.5','1.0','1.5','2.0'])

#helps to see the correlation of rankings and kills per death
ax3.bar(xaxis, df['K:D'],df['K:D'],width = 2,color = 'Green', label = 'K:D')
ax3.legend()

#Scatter Plot Average Combat Score
colors1 = np.where(df['ACS'] > 240 ,'saddlebrown' ,'sandybrown')
ax4.set_facecolor('peachpuff')
ax4.set_title('Average Combat Score')
ax4.set_xticks([1,250,500])
ax4.set_xticklabels(['1','250','500'])
ax4.set_xlabel('Player Rank')
ax4.set_ylabel('Avg Combat Score')
ax4.set_zlabel('Avg Combat Score')

#help to see that generally avg combat score correlates to rankings but itd definitly not a requirment to rank high
ax4.scatter(xaxis, df['ACS'],df['ACS'], color = colors1, label = 'ACS')
ax4.legend()

# the plot help show how first kill per round doesnt nessisarily correlate how good you are.
plt.show()
'''#plt.scatter(xaxis, df['ACS'], color = colors)'''