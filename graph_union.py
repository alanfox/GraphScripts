# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:02:47 2015

@author: af26
"""

import glob
import networkx as NX

path = 'C:/Users/af26/Documents/LarvalDispersalModel/Networkdata/*.graphml'
files = glob.glob(path)

G = NX.DiGraph()

for filename in files:
    infile = open(filename, 'r')
    H = NX.read_graphml(infile)
    infile.close()
    G = NX.compose(G, H)
    
outfile = open('C:/Users/af26/Documents/LarvalDispersalModel/Networkdata/graph20150114_3.graphml','w')
NX.write_graphml(G,outfile)
outfile.close()

outfile = open('C:/Users/af26/Documents/LarvalDispersalModel/Networkdata/graph201501014_3.gv','w')
NX.write_dot(G,outfile)
outfile.close()