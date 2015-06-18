# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX

    
filename = ('C:/Users/af26/Documents/LarvalDispersalModel' +
            '/polcoms1990/Run_20150402/Networkdata/GraphCompose/' +
            'graph_compose_latlon.graphml')

infile = open(filename, 'r')
H = NX.read_graphml(infile)
infile.close()

print H.nodes(data = True)

H.reverse(copy = False)

outfile = open('C:/Users/af26/Documents/LarvalDispersalModel' +
            '/polcoms1990/Run_20150402/Networkdata/GraphCompose/' +
            'graph_compose_latlon_reverse.graphml','w')
NX.write_graphml(H,outfile)
outfile.close()
