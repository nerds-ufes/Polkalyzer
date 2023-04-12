import pandas as pd
import seaborn as sns
import numpy as np
import lib.outputValidator as ov
from matplotlib import pyplot as plt

def StateOverheadHeatMap1(maxNodes,path):
    replicationArr = np.arange(1.0,2.0,0.1)
    newArr = []
    for i in range (1,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df['State Overhead'] = df.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    hMap = df1.pivot(index='Number of Nodes', columns='Replication Average per Node', values='State Overhead')
    #Plot Config 
    f, ax = plt.subplots(figsize=(10, 10))
    f.suptitle('State Overhead')
    #Plot Data
    sns.heatmap(data=hMap,
                cmap="rocket_r",  # Choose a squential colormap
                annot=False, # Label the maximum value
                #annot_kws={'fontsize':11},  # Reduce size of label to fit
                fmt='',          # Interpret labels as strings
                #square=True,     # Force square cells
                #vmax=500,         # Ensure same 
                #vmin=0,          # color scale
                linewidth=0.01,  # Add gridlines
                linecolor="#222",# Adjust gridline color
               )
    plt.gca().invert_yaxis()
    #Save Fig
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap1.png'),dpi=120)
    return hMap

def StateOverheadHeatMap2(df,path):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    df2['State Overhead'] = df2['State Overhead'].apply(lambda x: round(x, 1))
    df2['Replication Average per Node'] = df2['Replication Average per Node'].apply(lambda x: round(x, 1))
    hMap = df2.pivot_table(index='Number of Nodes', columns='Replication Average per Node', values='State Overhead', aggfunc='mean')
    #Plot Config
    fig= plt.subplots(figsize=(9,9))
    col_map = sns.hls_palette(h=.5,n_colors=6)
    #Plot Data
    sns.heatmap(data=hMap,
                cmap=col_map,  # Choose a squential colormap
                annot=False, # Label the maximum value
                #annot_kws={'fontsize':11},  # Reduce size of label to fit
                fmt='',          # Interpret labels as strings
                #square=True,     # Force square cells
                #vmax=500,         # Ensure same 
                #vmin=0,          # color scale
                linewidth=0.01,  # Add gridlines
                linecolor="#222",# Adjust gridline color
               )
    plt.gca().invert_yaxis()
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap2.png'),dpi=120)
    return hMap

def offsetAnnotation(x):
    newX = 0
    if(x == 1.0):
        newX = 0
    elif(x == 1.1):
        newX = 1
    elif(x == 1.2):
        newX = 2
    elif(x == 1.3):
        newX = 3
    elif(x == 1.4):
        newX = 4
    elif(x == 1.5):
        newX = 5
    elif(x == 1.6):
        newX = 6
    elif(x == 1.7):
        newX = 7
    elif(x == 1.8):
        newX = 8
    elif(x == 1.9):
        newX = 9
    elif(x == 2.0):
        newX = 10
    
    return newX


def StateOverheadHeatMap3(df,path):
    #Constants
    maxNodes = 30
    #Anotation DF
    df2 = (df[['Topology','Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    df2['State Overhead'] = df2['State Overhead'].apply(lambda x: round(x, 1))
    df2['Replication Average per Node'] = df2['Replication Average per Node'].apply(lambda x: round(x, 1))
    
    #Plot Config

    nodesArr = np.arange(1.5,31,1)
    nodesLabel = np.arange(1,31,1)
    replicationArr = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
    newArr = []
    for i in range (1,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df1 = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df1['State Overhead'] = df1.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    hMap = df1.pivot(index='Number of Nodes', columns='Replication Average per Node', values='State Overhead')
    #Plot Config 
    f, ax = plt.subplots(figsize=(10, 10))
    f.suptitle('Number of State Entries per Node using MPINT')
    plt.xlabel('Replication Average per Node')
    plt.ylabel('Number of Nodes')
    ax = sns.heatmap(data=hMap,cmap="rocket_r",fmt='.1f',annot=False,linewidth=0.01,linecolor="#222")
    #ax.set_xlim(xmin=0, xmax=10)
    #ax.set_xticks(replicationArr)
    #ax.set_xticklabels(replicationLabel)
    #ax.set_ylim(ymin=1, ymax=30)
    #ax.set_yticks(nodesArr)
    #ax.set_yticklabels(nodesLabel)
    #Plot Anotate
    offsetX = +0.5 #Centering the annotations
    offsetY = -0.5 #Centering the annotations
    for label, x, y in zip(df2['Topology'], df2['Replication Average per Node'], df2['Number of Nodes']):
        if(label == 'Gridnet' or label == 'Pern' or label == 'BtEurope' or label == 'EliBackbone' or label == 'Gambia' or label == 'Itnet' or label == 'Netrail' or label == 'Biznet'):
            x = offsetAnnotation(x)
            x += offsetX
            y += offsetY
            #ax.scatter(x,y, color = 'black')
            ax.annotate(
                label, 
                xy = (x, y), xytext = (40,15), xycoords='data',
                textcoords = 'offset points', ha = 'right', va = 'bottom',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    #plt.xlim([1.0,2.0])
    #plt.ylim([0,30])
    #Invert Y Axis
    plt.gca().invert_yaxis()
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap3.png'),dpi=120)
    return hMap

def StateOverheadHeatMap4(df,path):
    #Constants
    initialNode = 4
    maxNodes = 30
    #Anotation DF
    df2 = (df[['Topology','Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    df2['State Overhead'] = df2['State Overhead'].apply(lambda x: round(x, 1))
    df2['Replication Average per Node'] = df2['Replication Average per Node'].apply(lambda x: round(x, 1))
    
    #Plot Config

    #nodesArr = np.arange(1.5,31,1)
    replicationArr = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
    newArr = []
    for i in range (initialNode,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df1 = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df1['State Overhead'] = df1.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    hMap = df1.pivot(index='Number of Nodes', columns='Replication Average per Node', values='State Overhead')
    #Plot Config 
    plt.clf()
    plt.cla()
    f = plt.figure(figsize=(10,10))
    #f.suptitle('Number of State Entries per Node using MPINT')
    plt.xlabel('Replication Average per Node',fontsize=18)
    plt.ylabel('Number of Nodes',fontsize=18)
    #f.text(0.5, 0.04, 'Number of Nodes', ha='center',fontsize='18')
    #f.text(0.04, 0.5, 'Overhead (Bytes)', va='center', rotation='vertical',fontsize='18')
    #Plot HeatMap
    ax = sns.heatmap(data=hMap,cmap="rocket_r",fmt='.1f',annot=False,linewidth=0.01,linecolor="#222")
    #Plot Anotate
    offsetX = +0.5 #Centering the annotations
    offsetY = -0.5 -3 #Centering the annotations
    for label, x, y in zip(df2['Topology'], df2['Replication Average per Node'], df2['Number of Nodes']):
        if(label == 'Gridnet' or label == 'Atmnet' or label == 'BtEurope' or label == 'EliBackbone' or label == 'Gambia' or label == 'Itnet' or label == 'Netrail' or label == 'Abilene' or label == 'Sanren' or label == 'Cesnet1999' or label == 'Nsfnet' or label == 'Arpanet196912' or label == 'Arpanet19728' or label == 'Geant2001' or label == 'Cesnet1997' or label == 'Oxford' or label == 'Ibm' or label == 'Arn' or label == 'Renater2001' or label == 'Psinet' or label == 'Twaren'):
            x = offsetAnnotation(x)
            x += offsetX
            y += offsetY
            #ax.scatter(x,y, color = 'red')
            ax.annotate(
                label, 
                xy = (x, y), xytext = (0,0), xycoords='data',
                textcoords = 'offset points', ha = 'center', va = 'center',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))

    #plt.xlim([1.0,2.0])
    #plt.ylim([0,30])
    #Invert Y Axis
    plt.gca().invert_yaxis()
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap4.png'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap4.pdf'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    return hMap

def StateOverheadHeatMap5(df,path):
    #Constants
    initialNode = 4
    maxNodes = 30
    #Anotation DF
    df2 = (df[['Topology','Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    df2['State Overhead'] = df2['State Overhead'].apply(lambda x: round(x, 1))
    df2['Replication Average per Node'] = df2['Replication Average per Node'].apply(lambda x: round(x, 1))
    
    #Plot Config

    #nodesArr = np.arange(1.5,31,1)
    replicationArr = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
    newArr = []
    for i in range (initialNode,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df1 = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df1['State Overhead'] = df1.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    hMap = df1.pivot(index='Number of Nodes', columns='Replication Average per Node', values='State Overhead')
    #Plot Config 
    plt.clf()
    plt.cla()
    f = plt.figure(figsize=(10,10))
    #f.suptitle('Number of State Entries per Node using MPINT')
    plt.xlabel('Replication Average per Node',fontsize=18)
    plt.ylabel('Number of Nodes',fontsize=18)
    #f.text(0.5, 0.04, 'Number of Nodes', ha='center',fontsize='18')
    #f.text(0.04, 0.5, 'Overhead (Bytes)', va='center', rotation='vertical',fontsize='18')
    #Plot HeatMap
    ax = sns.heatmap(data=hMap,cmap="rocket_r",fmt='.1f',annot=False,linewidth=0.01,linecolor="#222")
    #Plot Anotate
    offsetX = +0.5 #Centering the annotations
    offsetY = -0.5 -3 #Centering the annotations
    for label, x, y in zip(df2['Topology'], df2['Replication Average per Node'], df2['Number of Nodes']):
        dfAux = df2.loc[df2['Number of Nodes'] == y]
        #print(dfAux)
        xMin = dfAux['Replication Average per Node'].min()
        xMax = dfAux['Replication Average per Node'].max()
        #print('Xmin Xmax:',xMin,xMax)
        x = offsetAnnotation(x)
        x += offsetX
        y += offsetY
        ax.scatter(x,y, color = 'black')
        if(label == 'Gridnet' or label == 'Atmnet' or label == 'BtEurope' or label == 'EliBackbone' or label == 'Gambia' or label == 'Itnet' or label == 'Netrail' or label == 'Abilene' or label == 'Sanren' or label == 'Cesnet1999' or label == 'Nsfnet' or label == 'Arpanet196912' or label == 'Arpanet19728' or label == 'Geant2001' or label == 'Cesnet1997' or label == 'Oxford' or label == 'Ibm' or label == 'Arn' or label == 'Renater2001' or label == 'Psinet' or label == 'Twaren'):
            ax.annotate(
                label, 
                xy = (x, y), xytext = (40,15), xycoords='data',
                textcoords = 'offset points', ha = 'right', va = 'bottom',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    #plt.xlim([1.0,2.0])
    #plt.ylim([0,30])
    #Invert Y Axis
    plt.gca().invert_yaxis()
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap5.png'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap5.pdf'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    return hMap

def StateOverheadHeatMap6(df,path):
    #Constants
    initialNode = 4
    maxNodes = 30
    #Anotation DF
    df2 = (df[['Topology','Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    df2['State Overhead'] = df2['State Overhead'].apply(lambda x: round(x, 1))
    df2['Replication Average per Node'] = df2['Replication Average per Node'].apply(lambda x: round(x, 1))
    
    #Plot Config

    #nodesArr = np.arange(1.5,31,1)
    replicationArr = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
    newArr = []
    for i in range (initialNode,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df1 = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df1['State Overhead'] = df1.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    hMap = df1.pivot(index='Number of Nodes', columns='Replication Average per Node', values='State Overhead')
    #Plot Config 
    plt.clf()
    plt.cla()
    f = plt.figure(figsize=(10,10))
    #f.suptitle('Number of State Entries per Node using MPINT')
    plt.xlabel('Replication Average per Node',fontsize=18)
    plt.ylabel('Number of Nodes',fontsize=18)
    #f.text(0.5, 0.04, 'Number of Nodes', ha='center',fontsize='18')
    #f.text(0.04, 0.5, 'Overhead (Bytes)', va='center', rotation='vertical',fontsize='18')
    #Plot HeatMap
    ax = sns.heatmap(data=hMap,cmap="rocket_r",fmt='.1f',annot=False,linewidth=0.01,linecolor="#222")
    #Plot Anotate
    offsetX = +0.5 #Centering the annotations
    offsetY = -0.5 -3 #Centering the annotations
    for label, x, y in zip(df2['Topology'], df2['Replication Average per Node'], df2['Number of Nodes']):
        dfAux = df2.loc[df2['Number of Nodes'] == y]
        #print(dfAux)
        xMin = dfAux['Replication Average per Node'].min()
        xMax = dfAux['Replication Average per Node'].max()
        #print('Xmin Xmax:',xMin,xMax)
        x = offsetAnnotation(x)
        x += offsetX
        y += offsetY
        if(label == 'Cesnet1999' or label == 'Nsfnet' or label == 'Arpanet196912' or label == 'Arpanet19728' or label == 'Geant2001' or label == 'Cesnet1997' or label == 'Ibm' or label == 'Renater2001'):
            ax.annotate(
                label, 
                xy = (x, y), xytext = (0,0), xycoords='data',
                textcoords = 'offset points', ha = 'center', va = 'center',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))
        else:
            ax.scatter(x,y, color = 'yellow')

    #plt.xlim([1.0,2.0])
    #plt.ylim([0,30])
    #Invert Y Axis
    plt.gca().invert_yaxis()
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap6.png'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HeatMap6.pdf'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    return hMap

def StateOverheadConcentration(df,path):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    #Plot Config
    f,axes= plt.subplots(1,2,sharey=True)
    f.suptitle('Concentration')
    axes[0].set_title('Number of Nodes')
    axes[1].set_title('Replication Average per Node')
    #Plot Data
    sns.ecdfplot(data=df2, x = "Number of Nodes",ax=axes[0]);
    sns.ecdfplot(data=df2, x = "Replication Average per Node",ax=axes[1]);
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_Concentration.png'),dpi=120)


def StateOverheadHistPlot(df,path):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    sns.histplot(x = 'Replication Average per Node', y = 'Number of Nodes', data = df2);
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_HP.png'),dpi=120)

def StateOverheadJointPlot(df,path):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    sns.jointplot(x = 'Replication Average per Node', y = 'Number of Nodes', data = df2,kind='hist');
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_JP.png'),dpi=120)


def StateOverheadDistribution(df,path):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    sns.relplot(x = 'Replication Average per Node', y = 'Number of Nodes', data = df2);
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/SO_Distribuition.png'),dpi=120)

def OverheadPointPlot(df,path):
    df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']]
    #Rename Dataframe
    df2.rename(columns = {'MPolka CRC8':'MPolKA-INT (CRC8)', 'MPolka CRC16':'MPolKA-INT (CRC16)','INT Clássico':'Original INT'}, inplace = True)
    #Melting dataframe
    dfm = df2.melt(id_vars=['Where','Number of Nodes'], var_name='Type', value_name='Overhead')
    dfm1 = dfm.loc[dfm['Where'] == 'DataPlane']
    dfm2 = dfm.loc[dfm['Where'] == 'ControlPlane']

    #Extract size of dataframe
    numberOfTopologys = int((len(df2.axes[0]))/2)
    #maxNode = df2['Number of Nodes'].max()
    #Plot Config
    f,ax= plt.subplots(2,1,figsize=(10,10),sharex=True)
    #f.suptitle('Overhead (Bytes) - %s Topologys' %numberOfTopologys)
    #plt.xlabel('Number of Nodes',fontsize=18)
    #plt.ylabel('Overhead',fontsize=18)
    f.text(0.5, 0.04, 'Number of Nodes', ha='center',fontsize=18)
    f.text(0.04, 0.5, 'Overhead (Bytes)', va='center', rotation='vertical',fontsize=18)
    #plt.xticks(np.arange(0, maxNode +1, 5))
    ax[0].set_title('DataPlane',fontsize=18)
    ax[1].set_title('ControlPlane',fontsize=18)
    #Plot Data
    g1 = sns.pointplot(x="Number of Nodes", y="Overhead", hue='Type',ax=ax[0],dodge=True, data=dfm1,errorbar=None);
    g1.set(xlabel=None,ylabel=None)
    g2 = sns.pointplot(x="Number of Nodes", y="Overhead", hue='Type',ax=ax[1],dodge=True,data=dfm2,errorbar=None);
    g2.set(xlabel=None,ylabel=None)
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/OverheadPP.png'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    plt.savefig(ov.toUniversalOSPath(f'{path}/OverheadPP.pdf'),bbox_inches='tight',pad_inches=0.1,dpi=120)

def OverheadLinePlot(df,path):
    df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']]
    #Rename Dataframe
    df2.rename(columns = {'MPolka CRC8':'INT-MPolKA (CRC8)', 'MPolka CRC16':'INT-MPolKA (CRC16)','INT Clássico':'INT Original'}, inplace = True)
    #Melting dataframe
    dfm = df2.melt(id_vars=['Where','Number of Nodes'], var_name='Type', value_name='Overhead')
    dfm1 = dfm.loc[dfm['Where'] == 'DataPlane']
    dfm2 = dfm.loc[dfm['Where'] == 'ControlPlane']

    #Extract size of dataframe
    numberOfTopologys = int((len(df2.axes[0]))/2)
    #Plot Config
    f,ax= plt.subplots(2,1,figsize=(10,10),sharex=True)
    #f.suptitle('Overhead (Bytes) (%s Topologys)' %numberOfTopologys)
    ax[0].set_title('DataPlane',fontsize=16)
    ax[1].set_title('ControlPlane',fontsize=16)
    #plt.xlabel('Number of Nodes',fontsize=18)
    #plt.ylabel('Overhead',fontsize=18)
    f.text(0.5, 0.04, 'Number of Nodes', ha='center',fontsize='18')
    f.text(0.04, 0.5, 'Overhead (Bytes)', va='center', rotation='vertical',fontsize='18')
    #Plot Data
    g1 = sns.lineplot(x="Number of Nodes", y="Overhead", hue='Type',ax=ax[0], data=dfm1,errorbar=None);
    g1.set(xlabel=None,ylabel=None)
    g2 = sns.lineplot(x="Number of Nodes", y="Overhead", hue='Type',ax=ax[1], data=dfm2,errorbar=None);
    g2.set(xlabel=None,ylabel=None)
    #Save Fig
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/OverheadLP.png'),bbox_inches='tight',pad_inches=0.1,dpi=120)
    plt.savefig(ov.toUniversalOSPath(f'{path}/OverheadLP.pdf'),bbox_inches='tight',pad_inches=0.1,dpi=120)

def OverheadCompare(df,path):
    df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT']]
    df2['Overhead'] = df2.apply(lambda x: x['MPolka CRC16'] - x['MPINT'],axis=1)
    df2['Number of Nodes'] = df2['Number of Nodes'].astype('float64')

    g = sns.relplot(
        data=df2,
        x="Number of Nodes", y="Overhead",
        hue="Where",
        height=4, aspect=.7, kind="line"
    )
    (g.map(plt.axhline, y=0, color=".7", dashes=(2, 1), zorder=0)
    .set_axis_labels("Number of Nodes", "Overhead")
    .set_titles("{Where}")
    .tight_layout(w_pad=0))

    dfDP = df2.loc[df2['Where'] == 'DataPlane']
    dfCP = df2.loc[df2['Where'] == 'ControlPlane']

    ##Plot Config
    #f,ax= plt.subplots(1,2,figsize=(10,5),sharey=True)
    #f.suptitle('Overhead')
    #ax[0].set_title('DataPlane')
    #ax[1].set_title('ControlPlane')
    ##Plot Data
    #sns.residplot(x="Number of Nodes", y="Overhead", data=dfDP);
    #sns.residplot(x="Number of Nodes", y="Overhead", data=dfCP);
    #Plot Data
    #sns.lineplot(x="Number of Nodes", y="Overhead",ax=ax, data=df2);
    ov.validateEntirePath(path)
    plt.savefig(ov.toUniversalOSPath(f'{path}/OverheadCompare-MPolka-MPINT.png'),dpi=120)
    return df2

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

def plotDataFrame(df,name,choice,algorithm,fixedNodeSender):

    if(choice == 1):
        OverheadPointPlot(df,ov.toUniversalOSPath(f'output/Plots/{name}'))
        #OverheadLinePlot(df,f'output/Plots/{name}')
        #OverheadCompare(df,f'output/Plots/{name}')
    elif(choice == 2):
        OverheadPointPlot(df,ov.toUniversalOSPath(f'output/Plots/{name}/{algorithm}/optimalNodeSender'))
        #OverheadLinePlot(df,f'output/Plots/{name}/{algorithm}/optimalNodeSender')
        #OverheadCompare(df,f'output/Plots/{name}/{algorithm}/optimalNodeSender')
    elif(choice == 3):
        OverheadPointPlot(df,ov.toUniversalOSPath(f'output/Plots/{name}/{algorithm}/{fixedNodeSender}'))
        #OverheadLinePlot(df,f'output/Plots/{name}/{algorithm}/{fixedNodeSender}')
        #OverheadCompare(df,f'output/Plots/{name}/{algorithm}/{fixedNodeSender}')

    StateOverheadJointPlot(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadConcentration(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadDistribution(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadHeatMap2(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadHeatMap3(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadHeatMap4(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadHeatMap5(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))
    StateOverheadHeatMap6(df,ov.toUniversalOSPath(f'output/Plots/{name}/StateOverhead'))