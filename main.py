import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

import lib.toDataframe as tdf
import lib.toProbe as tpb
from lib.readTopologyZoo import removeBadValues

#print('Digite o nó que enviará a sonda em G: ')
#node = int(input())

df = pd.DataFrame(columns=['Topology','Where','IsBackBone','Number of Nodes','Number of Edges','Replication Average per Node','Max Replication','State Overhead','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']) #Empty Row Dataframe

GIsis = nx.from_edgelist([[1,5],[5,3],[1,2],[2,6],[6,4],[6,7]])
sondaIsis = tpb.dfs_init(GIsis,1)
#print('Matriz de Sondas Isis = ',sondaIsis,'\n')

df = tdf.toDataframe(df,'Isis',1,7,6) #DataFrame Isis Example
df = tdf.appendAllTopologysToDataFrame(df)
df.to_csv('OptimalOverhead.csv',index=False)


######################################## PLOT AREA #################################################

#sns.catplot(x="Topology", y="MPolka CRC8", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()
#sns.catplot(x="Topology", y="MPolka CRC16", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()
#sns.catplot(x="Topology", y="MPINT", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()
#sns.catplot(x="Topology", y="INT Clássico", hue="Where",kind="bar", data=df, errorbar = None);
#plt.show()

df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']]
dfm = df2.melt(id_vars=['Where','Number of Nodes'], var_name='Type', value_name='Overhead')
#sns.catplot(x="Number of Nodes", y="Overhead", hue='Type', data=dfm, kind='point');
sns.pointplot(x="Number of Nodes", y="Overhead", hue=dfm[['Type','Where']].apply(tuple,axis=1), data=dfm);
plt.savefig('plots/withNodeOptimization.png')
#df2.sort_values(by=['Number of Nodes'],inplace=True)
#df2 = df2.set_index('Number of Nodes')
#df2.plot()
#plt.show()
#hMap = StateOverheadHeatMap(maxNodes=50,maxReplication=2.0)


