# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX
from alpha_centrality import alpha_centrality
        
root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms1990/Run_1000_longlife/')

filename = (root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon_alpha.graphml')

infile = open(filename, 'r')
H = NX.read_graphml(infile)
infile.close()

H.remove_edges_from(H.selfloop_edges())

print H.nodes(data = True)

betweenness = alpha_centrality(NX.reverse(H),0.2,evalue = 'alpha_exogenous')

print betweenness

NX.set_node_attributes(H, 'alpha_centrality', betweenness)

print H.nodes(data=True)

#outfile = open(root_folder + 'Networkdata/GraphCompose/' +
#            'graph_compose_latlon_percolation_centrality.graphml','w')
#NX.write_graphml(H,outfile)
#outfile.close()
outfile = open(root_folder + 'Networkdata/GraphCompose/' +
                'graph_compose_latlon_centralities.gexf','w')
NX.write_gexf(H,outfile)
outfile.close()