import lib.plots as pplt
import lib.menu as menu
from lib.style import greetings

choice=menu.mainMenu()
if(choice == 1):
    df,choice,algorithm,fixedNodeSender = menu.algorithmChoice()
elif(choice == 2):
    menu.topologyChoice()


##### PLOT AREA #####

if(choice == 1): # Only if plot exists
    slice30 = df.loc[df['Number of Nodes'] <= 30].copy()
    slice50 = df.loc[df['Number of Nodes'] <= 50].copy()
    pplt.plotDataFrame(slice30,name='Slice30',choice=1,algorithm=None,fixedNodeSender=None) #Ignore algorithm and fixedNodeSender parameters, no matter for us if choice == 1
    pplt.plotDataFrame(slice50,name='Slice50',choice=1,algorithm=None,fixedNodeSender=None) #Ignore algorithm and fixedNodeSender parameters, no matter for us if choice == 1

greetings()