# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX
from alpha_centrality import alpha_centrality

graph_filter = True
        
root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms1990to2000_climatology/Run_1000_baseline/')

filename = (root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon_alpha.graphml')

infile = open(filename, 'r')
H = NX.read_graphml(infile)
infile.close()

H.remove_edges_from(H.selfloop_edges())

#print H.nodes(data = True)

# code to filter by alpha_exogenous. Above 0.6 removes all sites without
# observations (includes uncertain observations)

if graph_filter:
    G = NX.DiGraph()
    for n,d in H.nodes_iter(data= True):
        if d['alpha_exogenous'] >= 0.6:
            G.add_node(n,d)
    for u,v,d in H.out_edges_iter(data = True):
        if u in G.nodes() and v in G.nodes():
            G.add_edge(u,v,d)
    H = G        

#print H.nodes(data=True)        

betweenness = alpha_centrality(NX.reverse(H),0.2,evalue = 'alpha_exogenous')

print betweenness

NX.set_node_attributes(H, 'alpha_centrality', betweenness)

#print H.nodes(data=True)

#outfile = open(root_folder + 'Networkdata/GraphCompose/' +
#            'graph_compose_latlon_percolation_centrality.graphml','w')
#NX.write_graphml(H,outfile)
#outfile.close()
outfile = open(root_folder + 'Networkdata/GraphCompose/' +
                'graph_compose_latlon_centralities_alpha0.1_filt.gexf','w')
NX.write_gexf(H,outfile)
outfile.close()