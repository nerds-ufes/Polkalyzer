import pandas as pd
import seaborn as sns
import numpy as np
import lib.outputValidator as ov
from matplotlib import pyplot as plt

def StateOverheadHeatMap1(maxNodes,maxReplication):
    replicationArr = np.arange(1.0,maxReplication,0.1)
    newArr = []
    for i in range (1,maxNodes+1):
        for j in replicationArr:
            newArr.append([i,round(j,1)])

    df = pd.DataFrame(data=newArr,columns=['Number of Nodes','Replication Average per Node'])
    df['State Overhead'] = df.apply(lambda x : x['Number of Nodes']*(1+2*(x['Replication Average per Node'])),axis=1)
    hMap = df.pivot('Number of Nodes','Replication Average per Node','State Overhead')
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
    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/StateOverheadHeatMap1.png',dpi=120)
    return hMap

def StateOverheadHeatMap2(df):
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
    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/StateOverheadHeatMap2.png',dpi=120)
    return hMap

def StateOverheadConcentration(df):
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
    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/StateOverheadConcentration.png',dpi=120)


def StateOverheadHistPlot(df):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    sns.histplot(x = 'Replication Average per Node', y = 'Number of Nodes', data = df2);
    #Save Fig
    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/StateOverheadHistPlot.png',dpi=120)

def StateOverheadJointPlot(df):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    sns.jointplot(x = 'Replication Average per Node', y = 'Number of Nodes', data = df2,kind='hist');
    #Save Fig
    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/StateOverheadJointPlot.png',dpi=120)


def StateOverheadDistribution(df):
    df2 = (df[['Number of Nodes','Replication Average per Node','State Overhead']].loc[df['Where'] == 'DataPlane']).copy() #To exclude duplicated values, we look only for DataPlane
    sns.relplot(x = 'Replication Average per Node', y = 'Number of Nodes', data = df2);
    plt.show()

def OverheadPointPlot(df):
    df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']]
    dfm = df2.melt(id_vars=['Where','Number of Nodes'], var_name='Type', value_name='Overhead')
    sns.pointplot(x="Number of Nodes", y="Overhead", hue=dfm[['Type','Where']].apply(tuple,axis=1), data=dfm);

    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/OverheadWithNodeOptimization.png')
    #df2.sort_values(by=['Number of Nodes'],inplace=True)
    #df2 = df2.set_index('Number of Nodes')
    #df2.plot()

def OverheadLinePlot(df):
    df2 = df[['Where','Number of Nodes','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']]
    dfm = df2.melt(id_vars=['Where','Number of Nodes'], var_name='Type', value_name='Overhead')
    dfm1 = dfm.loc[dfm['Where'] == 'DataPlane']
    dfm2 = dfm.loc[dfm['Where'] == 'ControlPlane']

    #Plot Config
    f,ax= plt.subplots(1,2,figsize=(10,5),sharey=True)
    f.suptitle('Overhead')
    ax[0].set_title('DataPlane')
    ax[1].set_title('ControlPlane')
    #Plot Data
    sns.lineplot(x="Number of Nodes", y="Overhead", hue='Type',ax=ax[0], data=dfm1);
    sns.lineplot(x="Number of Nodes", y="Overhead", hue='Type',ax=ax[1],data=dfm2);
    #Save Fig
    ov.validateEntirePath('output/Plots/')
    plt.savefig('output/Plots/OverheadWithNodeOptimization2.png',dpi=120)

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