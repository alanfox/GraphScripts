# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import glob
import networkx as NX

root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms2000/Run_1000_baseline/')

path = (root_folder + 'Networkdata/*.graphml')
files = glob.glob(path)

G = NX.DiGraph()

for filename in files:
    print filename
    infile = open(filename, 'r')
    H = NX.read_graphml(infile)
    infile.close()
    G = NX.compose(G, H)
    
outfile = open(root_folder + 'Networkdata/GraphCompose/' +
               'graph_compose.graphml','w')
NX.write_graphml(G,outfile)
outfile.close()

outfile = open(root_folder + 'Networkdata/GraphCompose/' +
                'graph_compose.gexf','w')
NX.write_gexf(G,outfile)
outfile.close()