import networkx as nx
import os
import shutil
from pathlib import Path

# Util because lots of graphs are with non consecutive labels in gml
def remap_labels(G):
    return nx.convert_node_labels_to_integers(
        G,
        first_label=0,
        ordering='default',
        label_attribute='old_label'
    )

# Install behavioral model
def installBehavioralModel():
    # Verify if folder exists
    if not os.path.exists(Path('lib/p4/bmv2')):
        # Clone repo bmv2
        os.system('git clone https://github.com/p4lang/behavioral-model.git --depth 1 bmv2')
        # Move folder to lib
        shutil.move('bmv2', Path('lib/p4/bmv2'))
        # Rename without using os, because it's not working on Windows
        # shutil.move('lib/p4/bmv2/targets/simple_switch/simple_switch_CLI.in', 'lib/p4/bmv2/targets/simple_switch/simple_switch')
