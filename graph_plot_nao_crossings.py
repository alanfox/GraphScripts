# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:54:02 2015

@author: af26

Takes connectivity graphs for several years and combines them into a single 
graph. Two edge weights are given: one is a sum of the weights in the 
years, the other is the number of years when the connection exists.
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
from scipy import signal
import scipy.stats as stats

def read_nao_monthly(filename):
    year = []
    month = []
    nao = []
    for line in infile:
        wordlist = line.split()
        year.append(int(wordlist[0]))
        month.append(int(wordlist[1]))
        nao.append(float(wordlist[2]))
    return year, month, nao
    
filename = ('C:/Users/af26/NAO/nao_monthly.txt')
infile = open(filename,'r')

yr, mon, nao = read_nao_monthly(infile)

startyear = 1965
endyear = 2004

years = range(startyear,endyear+1)
print_years = list(years)
print_years.insert(0,'years')

nao_jan = np.array([nao[i] for i in range(len(nao)) 
            if mon[i] == 1 and yr[i] >= startyear and yr[i] <= endyear])
nao_feb = np.array([nao[i] for i in range(len(nao)) 
            if mon[i] == 2 and yr[i] >= startyear and yr[i] <= endyear])
nao_mar = np.array([nao[i] for i in range(len(nao)) 
            if mon[i] == 3 and yr[i] >= startyear and yr[i] <= endyear])
nao_apr = np.array([nao[i] for i in range(len(nao)) 
            if mon[i] == 4 and yr[i] >= startyear and yr[i] <= endyear])

nao_meanfm = (nao_mar)


#release_site = ['Anton Dohrn Seamount','Darwin Mounds','East Mingulay',
#                'East Rockall Bank','Faroe-Shetland Sponge Belt',
#                'Hatton Bank','North West Rockall Bank',
#                'Rosemary Bank Seamount','South-East Rockall Bank SAC',
#                'Wyville Thomson Ridge']

release_site = ['Anton Dohrn Seamount','Darwin Mounds',
                'East Rockall Bank','Faroe-Shetland Sponge Belt',
                'Hatton Bank','North West Rockall Bank',
                'Rosemary Bank Seamount','South-East Rockall Bank SAC',
                'Wyville Thomson Ridge','East Mingulay']

with open('doublelife_nao_mar.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(print_years)
    x = nao_jan.tolist()
    x.insert(0,'NAO Jan')
    writer.writerow(x)
    x = nao_feb.tolist()
    x.insert(0,'NAO Feb')
    writer.writerow(x)
    x = nao_mar.tolist()
    x.insert(0,'NAO Mar')
    writer.writerow(x)
    x = nao_apr.tolist()
    x.insert(0,'NAO Apr')
    writer.writerow(x)

    print_header1 = ['Section',
                    'A1','','A2','','A3','','A4','','A5','','A6','',
                    'B1','','B2','','B3','','B4','','B5','','B6','',
                    'c1','',
                    'S1','','S2','','S3','','S4','',
                    ]    
    print_header2 = ['Correlation',
                    'r','p','r','p','r','p','r','p','r','p','r','p',
                    'r','p','r','p','r','p','r','p','r','p','r','p',
                    'r','p',
                    'r','p','r','p','r','p','r','p',
                    ]    
    
    with open('doublelife_nao_mar_correlations.csv', 'wb') as g:
        writer2 = csv.writer(g)
        writer2.writerow(print_header1)
        writer2.writerow(print_header2)
        
        nint = len(years)
        
        for site in release_site:
            print site
            a1 = np.zeros(nint)
            a2 = np.zeros(nint)
            a3 = np.zeros(nint)
            a4 = np.zeros(nint)
            a5 = np.zeros(nint)
            a6 = np.zeros(nint)
            b1 = np.zeros(nint)
            b2 = np.zeros(nint)
            b3 = np.zeros(nint)
            b4 = np.zeros(nint)
            b5 = np.zeros(nint)
            b6 = np.zeros(nint)
            c1 = np.zeros(nint)
            s1 = np.zeros(nint)
            s2 = np.zeros(nint)
            s3 = np.zeros(nint)
            s4 = np.zeros(nint)
            
            f, axarr = plt.subplots(2)
            
            for year in years:
                i = year - startyear
                graph_file = ('X:/Lophelia Share/Alan/LarvalDispersalResults/' + 
                                'polcoms' + str(year) + 
                                '/Run_1000_doublelife/Crossingdata/' + 
                                site + '_crosses.graphml')
                infile = open(graph_file,'r')                
                G = nx.read_graphml(infile)
                infile.close()
                   
                for u,v,data in G.edges_iter(data=True):
                    if v == 'A1':
                        a1[i] = data['nstayed']
                    if v == 'A2':
                        a2[i] = data['nstayed']
                    if v == 'A3':
                        a3[i] = data['nstayed']
                    if v == 'A4':
                        a4[i] = data['nstayed']
                    if v == 'A5':
                        a5[i] = data['nstayed']
                    if v == 'A6':
                        a6[i] = data['nstayed']
                    if v == 'B1':
                        b1[i] = data['nstayed']
                    if v == 'B2':
                        b2[i] = data['nstayed']
                    if v == 'B3':
                        b3[i] = data['nstayed']
                    if v == 'B4':
                        b4[i] = data['nstayed']
                    if v == 'B5':
                        b5[i] = data['nstayed']
                    if v == 'B6':
                        b6[i] = data['nstayed']
                    if v == 'C1':
                        c1[i] = data['nstayed']
                    if v == 'S1':
                        s1[i] = data['nstayed']
                    if v == 'S2':
                        s2[i] = data['nstayed']
                    if v == 'S3':
                        s3[i] = data['nstayed']
                    if v == 'S4':
                        s4[i] = data['nstayed']
                                               
    #        axarr[0].plot(years,nao_meanfm * 200.0)
    #        axarr[0].plot(years,pent)
    #        axarr[0].plot(years,o2s)
    #        axarr[0].plot(years,s2nc)
    #        axarr[0].plot(years,nc2n)
            axarr[0].plot(years,s4)
            axarr[0].set_title('Larvae crossing S4 from ' + site)
            
            axarr[1].plot(years,nao_meanfm)
    #        axarr[1].plot(years,nao_jan)
    #        axarr[1].plot(years,nao_feb)
    #        axarr[1].plot(years,nao_mar)
    #        axarr[1].plot(years,nao_apr)
                    
            axarr[1].set_title('NAO index, March average')
            
            
            writer.writerow([site])
            x = a1.tolist()
            x.insert(0,'A1')
            writer.writerow(x)
            x = a2.tolist()
            x.insert(0,'A2')
            writer.writerow(x)
            x = a3.tolist()
            x.insert(0,'A3')
            writer.writerow(x)
            x = a4.tolist()
            x.insert(0,'A4')
            writer.writerow(x)
            x = a5.tolist()
            x.insert(0,'A5')
            writer.writerow(x)
            x = a6.tolist()
            x.insert(0,'A6')
            writer.writerow(x)
            x = b1.tolist()
            x.insert(0,'B1')
            writer.writerow(x)
            x = b2.tolist()
            x.insert(0,'B2')
            writer.writerow(x)
            x = b3.tolist()
            x.insert(0,'B3')
            writer.writerow(x)
            x = b4.tolist()
            x.insert(0,'B4')
            writer.writerow(x)
            x = b5.tolist()
            x.insert(0,'B5')
            writer.writerow(x)
            x = b6.tolist()
            x.insert(0,'B6')
            writer.writerow(x)
            x = c1.tolist()
            x.insert(0,'C1')
            writer.writerow(x)
            x = s1.tolist()
            x.insert(0,'S1')
            writer.writerow(x)
            x = s2.tolist()
            x.insert(0,'S2')
            writer.writerow(x)
            x = s3.tolist()
            x.insert(0,'S3')
            writer.writerow(x)
            x = s4.tolist()
            x.insert(0,'S4')
            writer.writerow(x)
            
            cor = []
            x = stats.pearsonr(nao_meanfm,a1)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,a2)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,a3)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,a4)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,a5)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,a6)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,b1)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,b2)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,b3)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,b4)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,b5)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,b6)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,c1)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,s1)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,s2)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,s3)
            cor.append(x[0])
            cor.append(x[1])
            x = stats.pearsonr(nao_meanfm,s4)
            cor.append(x[0])
            cor.append(x[1])
            cor.insert(0,site)
            writer2.writerow(cor)
            
    #        nao_meanfm_dt = signal.detrend(nao_meanfm)
    #        
    #        df_nao = pd.DataFrame([nao_meanfm,s4])
    #        df_naoT = df_nao.T
    #        df_total = pd.DataFrame(total)
    #        
    #        cor = df_naoT.corr()
    #        print cor
            
            print stats.pearsonr(nao_meanfm,s4)
    
