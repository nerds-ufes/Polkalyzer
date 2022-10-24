import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def StateOverheadHeatMap(maxNodes,maxReplication):
    replicationArr = np.arange(1.0,maxReplication,0.1)
    newArr = []
    for i in range (1,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df['State Overhead'] = df.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    heatMap = df.pivot('Number of Nodes','Replication Average per Node','State Overhead')
    sns.heatmap(data=heatMap, annot=False, fmt="f", vmin=-0.05,cmap="rocket_r")
    plt.gca().invert_yaxis()
    plt.show()
    return heatMap