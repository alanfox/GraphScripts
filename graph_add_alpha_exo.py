# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX
import csv

file_dir = 'C:/Users/af26/ProtectedAreaData/'

        
root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms1990/Run_1000_longlife/')

filename = (root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon.graphml')

percolationfile = (file_dir + 'lophelia_percolation_state.csv')


# read coordinates of mpa centres into a dictionary 

percolation = {}

infile = open(filename, 'r')
H = NX.read_graphml(infile)
infile.close()

for node in H.nodes():
    percolation[node] = 0.0
print percolation

with open(percolationfile, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        percolation[row[0]] = float(row[1])
        
for p in percolation:
    percolation[p] = percolation[p] + 0.1
print percolation

for node in H.nodes():
    H.node[node]['alpha_exogenous'] = percolation[node]
print H.nodes(data=True)

outfile = open(root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon_alpha.graphml','w')
NX.write_graphml(H,outfile)
outfile.close()
