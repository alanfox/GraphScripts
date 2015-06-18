# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 11:59:44 2015

@author: af26
"""

import networkx as NX

import numpy as np



# import the graph

infile = open('C:/Users/af26/Documents/LarvalDispersalModel/'
                + 'polcoms1996_20150224/Networkdata/GraphCompose/'
                + 'graph20150224.graphml','r')
G = NX.read_graphml(infile)
infile.close()

H = NX.convert_node_labels_to_integers(G, first_label=0, ordering='sorted', 
                                       label_attribute='Name')

print NX.betweenness_centrality(G)

print NX.closeness_centrality(G)

print NX.eigenvector_centrality(G, max_iter = 1000)



    # set up array of zeros
    
