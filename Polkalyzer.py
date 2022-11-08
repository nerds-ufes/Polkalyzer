import lib.plots as pplt
import lib.menu as menu

df,choice,algorithm,fixedNodeSender = menu.mainMenu()

##### PLOT AREA ####

slice30 = df.loc[df['Number of Nodes'] <= 30]
slice50 = df.loc[df['Number of Nodes'] <= 50]
pplt.plotDataFrame(slice30,name='Slice30',choice=1,algorithm=None,fixedNodeSender=None) #Ignore algorithm and fixedNodeSender parameters, no matter for us if choice == 1
pplt.plotDataFrame(slice50,name='Slice50',choice=1,algorithm=None,fixedNodeSender=None) #Ignore algorithm and fixedNodeSender parameters, no matter for us if choice == 1