# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import networkx as NX
import csv

root_folder = ('C:/Users/af26/LarvalDispersalResults/' +
            'polcoms1990to2000/Run_1000_baseline/')

# read coordinates of mpa centres into a dictionary 

latlonfile = ('C:/Users/af26/ProtectedAreaData/mpa_central_latlon.txt')
csvfile = open(latlonfile, 'r')

csvreader = csv.reader(csvfile, delimiter='\t')

temp = []
for row in csvreader:
    temp.append(row)
    
csvfile.close()

latlon = {}
for i in range(1,len(temp)):
    latlon[temp[i][0]] = [float(temp[i][1]),float(temp[i][2])]
    
filename = (root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose.graphml')

infile = open(filename, 'r')
H = NX.read_graphml(infile)
infile.close()

for node in H.nodes():
    
    H.node[node]['latitude'] = latlon[node][1]
    H.node[node]['longitude'] = latlon[node][0]


print H.nodes(data = True)

outfile = open(root_folder + 'Networkdata/GraphCompose/' +
            'graph_compose_latlon.graphml','w')
NX.write_graphml(H,outfile)
outfile.close()
