# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX
import csv

root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms1995/Run_1000_baseline/')

# read coordinates of mpa centres into a dictionary 
    
filename = (root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon_centralities.gexf')

infile = open(filename, 'r')
H = NX.read_gexf(infile)
infile.close()

for edge in H.edges():
    H.edge[edge[0]][edge[1]]['weight'] = (H.edge[edge[0]][edge[1]]['weight'] 
                                            * 1000.0)

print H.edges(data = True)

outfile = open(root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon_centralities_weightppt.gexf','w')
NX.write_gexf(H,outfile)
outfile.close()
