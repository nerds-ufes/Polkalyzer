import networkx as nx

# Util because lots of graphs are with non consecutive labels in gml
def remap_labels(G):
    return nx.convert_node_labels_to_integers(
        G,
        first_label=0,
        ordering='default',
        label_attribute='old_label'
    )
