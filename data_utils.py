import os
from graph import DirectedGraph, Node, Edge

def load_linqs_data(content_file, cites_file):
    
    if not os.path.isfile(content_file):
        raise IOError('No content file')
        return
    
    if not os.path.isfile(cites_file):
        raise IOError('No cites file')
        return
        
    graph = DirectedGraph()
    domain_labels = []


    content_file_reader = open(content_file, 'r')


    for line_str in content_file_reader:
        tokens = line_str.split('\t')
        
        node_id = tokens[0]
        feature_vector = tokens[1:-1]
        label = tokens[-1].strip()
        
        new_node = Node(node_id, feature_vector, label)
        graph.add_node(new_node)

        domain_labels.append(tokens[-1].strip())
    
    cites_file_reader = open(cites_file, 'r')
    citations = dict()

    for line in cites_file_reader:
        tokens2 = line.split('\t')

        from_node = tokens2[1].strip()
        to_node = tokens2[0].strip()
        endge = Edge(from_node, to_node)
        graph.add_edge(endge)    

    return graph, set(domain_labels)