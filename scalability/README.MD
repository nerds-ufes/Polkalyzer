# Polkalyzer - Polka analyzer tool for any given topology.

![Polkalyzer Explained](./imgs/PolkalyzerBehavior.png)
Diagram explaining polkalyzer behavior.

_This tool can be dissecated in multiple parts._ <br>
**Filter Raw Topologies Dataset:** <br>
1 - Load topologys dataset with NetworkX.
2 - Remove topologys that can't be read by multiple factors. <br>
3 - Remove topologys that are disconnected graphs. <br>
**Transform a Graph into a MST:** <br>
4 - Transform GML Files that represent a topology into a **minimum spanning tree (MST)**. <br>
You can choose what MST Algorithm you want avaible in networkx.<br>
**Extract Probe Matrix:** <br>
5 - Perform a **DFS** in extracted MST to **simulate probes** from different telemetry approaches. <br>
You can choose the a fixed node sender or leave to algorithm decide the optimal node sender for all given topologies. <br>
**Fill the dataframe until there are no more unread topologies** <br>
6 - While algorithm is performing a DFS, the algorithm will extract a lot of usefull information about each graph and fill it the dataframe. <br>
**Data Export:** <br>
7 - Export to **output/Topology** MPolKA-INT/MPINT probes to all topologys given in topologyZoo. <br> 
8 - Export to **output/Data** all usefull information collected into a csv. <br>
9 - Export to **output/Plots** different plots to help us to understand the information collected. <br>

## Polkalyzer dependencies
You will need Python3 to run Polkalyzer, so try it:
```
python --version
python3 --version
```
If you haven't it, try install:
https://www.python.org/downloads/

You also will need PIP dependencies:
```sh
pip3 install --upgrade pip
pip3 install pandas, seaborn, matplotlib, networkx
```

**Only for Windows Users**, check your enviroment variables:
```sh
- Enviroment Variables:
    Add to PATH:
    C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310
    C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310\Scripts
- New System Variable:
    Name: PYTHONUTF8
    Value: 1
```

## Using Polkalyzer
First of all, run Polkalyzer.py
```
python3 Polkalyzer.py
```

![Algorithm Choice](./imgs/AlgorithmChoice.png)
You can choose three of these options, after chosen check your output folder.
# References
Topology Dataset - http://www.topology-zoo.org/dataset.html