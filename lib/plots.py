import pandas as pd
import seaborn as sns
import numpy as np
import lib.outputValidator as ov
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

    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/StateOverheadHeatMap.png')
    return heatMap

def OverheadPointPlot(df):
    df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']]
    dfm = df2.melt(id_vars=['Where','Number of Nodes'], var_name='Type', value_name='Overhead')
    sns.pointplot(x="Number of Nodes", y="Overhead", hue=dfm[['Type','Where']].apply(tuple,axis=1), data=dfm);

    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/OverheadWithNodeOptimization.png')
    #df2.sort_values(by=['Number of Nodes'],inplace=True)
    #df2 = df2.set_index('Number of Nodes')
    #df2.plot()

######################################## PLOT AREA #################################################

#sns.catplot(x="Topology", y="MPolka CRC8", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()
#sns.catplot(x="Topology", y="MPolka CRC16", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()
#sns.catplot(x="Topology", y="MPINT", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()
#sns.catplot(x="Topology", y="INT Clássico", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()

#sns.catplot(x="Number of Nodes", y="Overhead", hue='Type', data=dfm, kind='point');
#plt.show()