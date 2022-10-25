# Polkalyzer - Polka analyzer tool for any given topology.
_This tool can be dissecated in multiple parts_ <br>
**Download and Filter:** <br>
1 - Download all graphs (.gml) avaible in topologyZoo. <br>
2 - Remove topologys that can't be read by multiple factors. <br>
3 - Filter same topologys to your newest version. <br>
**Transform a Graph into a probe:** <br>
4 - Transform GML Files that represent a topology into a **minimum spanning tree (MST)**. <br>
You can choose what MST Algorithm you want avaible in networkx.<br>
5 - Perform a **DFS** in extracted MST to **simulate probes** from different SR Approaches. <br>
You can choose the a fixed node sender or leave to algorithm decide the optimal node sender for all given topologys. <br>
**Generate a DataFrame** <br>
6 - While algorithm is performing a DFS, the algorithm will extract a lot of usefull information about each graph. <br>
**Data Export:** <br>
7 - Export to **output/Topology** MPolka/MPINT probes to all topologys given in topologyZoo. <br> 
8 - Export to **output/Data** the information collected into a csv. <br>
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
pip3 install pandas, seaborn, matplotlib, requests, html5lib, networkx
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

# References
Topology Dataset - http://www.topology-zoo.org/dataset.html