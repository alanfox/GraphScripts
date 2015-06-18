# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 11:59:44 2015

@author: af26
"""

import networkx as NX
import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


SORT = False

cdict = {'red': ((0.0, 0.96, 0.96),
                 (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.8, 0.9),
                   (1.0, 0.0, 0.0)),
         'blue': ((0.0, 0.6, 0.6),
                 (1.0, 0.0, 0.0))}
my_cmap = col.LinearSegmentedColormap('my_colormap',cdict,256)

# import the graph

infile = open('C:/Users/af26/Documents/LarvalDispersalModel/'
                + 'polcoms1996_20150224/Networkdata/GraphCompose/'
                + 'graph20150224.graphml','r')
G = NX.read_graphml(infile)
infile.close()

H = NX.convert_node_labels_to_integers(G, first_label=0, ordering='sorted', 
                                       label_attribute='Name')

    # set up array of zeros
    
x = np.zeros((len(H.nodes()),len(H.nodes())), dtype = float)


if SORT:

    # need to set mpa order for a good plot. Grouping geographically related mpas
    # order has been set out in a file
    
    infile = open('C:/Users/af26/Documents/LarvalDispersalModel/Networkdata/'
                    + '/1000larvae_1/sorted_mpa_list.txt','r')
    sorted_mpas = infile.readlines()
    infile.close()
    
    # strip out line breaks
    for i in range(len(sorted_mpas)):
        sorted_mpas[i] = sorted_mpas[i][0:-1]
                                     
    # map from H integer node label to position in sorted list
    imap = []
    
    for i,d in H.nodes(data = True):
        j = sorted_mpas.index(d['Name'])
        imap.append(j)
        
    for i,j,d in H.edges(data = True):
        ii = imap[i]
        jj = imap[j]
        x[jj,ii] = d['weight']
        
else:
    sorted_mpas = []   
    for i, d in H.nodes(data = True):
        sorted_mpas.append(d['Name'])
        
    x = NX.to_numpy_matrix(H).getA()
      
# mask zeros (no connection) for a clearer plot    
y = np.ma.masked_where(x < 0.001, x)

plt.pcolormesh(y,cmap=my_cmap,edgecolor = 'k')
plt.colorbar()
plt.axis([0,len(H.nodes()),0,len(H.nodes())])
plt.xticks(np.arange(0.5,len(H.nodes())+0.5), sorted_mpas, rotation = 90)
plt.yticks(np.arange(0.5,len(H.nodes())+0.5), sorted_mpas)
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.3)
plt.show()
    
    