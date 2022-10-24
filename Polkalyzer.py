import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

import lib.toDataframe as tdf
import lib.toProbe as tpb
import lib.plots as pplt
import lib.outputValidator as ov
from lib.readTopologyZoo import removeBadValues

#print('Digite o nó que enviará a sonda em G: ')
#node = int(input())

df = pd.DataFrame(columns=['Topology','Where','IsBackBone','Number of Nodes','Number of Edges','Replication Average per Node','Max Replication','State Overhead','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']) #Empty Row Dataframe


#ISIS EXAMPLE
GIsis = nx.from_edgelist([[1,5],[5,3],[1,2],[2,6],[6,4],[6,7]])
sondaIsis = tpb.dfs_init(GIsis,1)
df = tdf.toDataframe(df,'Isis',1,7,6) #DataFrame Isis Example
#print('Matriz de Sondas Isis = ',sondaIsis,'\n')

#DataFrame Area

df = tdf.appendAllTopologysToDataFrame(df)
ov.validateEntirePath('output/Databases/')
df.to_csv('output/Databases/OptimalOverhead.csv',index=False)

#Plot Area

pplt.OverheadPointPlot(df)
#pplt.StateOverheadHeatMap(maxNodes=50,maxReplication=2.0)
