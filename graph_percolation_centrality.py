# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX
from percolation_centrality import percolation_centrality
        
root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms1995/Run_1000_baseline/')

filename = (root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon_percolation.graphml')

infile = open(filename, 'r')
H = NX.read_graphml(infile)
infile.close()

betweenness = percolation_centrality(H)

print betweenness

NX.set_node_attributes(H, 'percolation_centrality', betweenness)

print H.nodes(data=True)

#outfile = open(root_folder + 'Networkdata/GraphCompose/' +
#            'graph_compose_latlon_percolation_centrality.graphml','w')
#NX.write_graphml(H,outfile)
#outfile.close()
outfile = open(root_folder + 'Networkdata/GraphCompose/' +
                'graph_compose_latlon_percolation_centrality.gexf','w')
NX.write_gexf(H,outfile)
outfile.close()