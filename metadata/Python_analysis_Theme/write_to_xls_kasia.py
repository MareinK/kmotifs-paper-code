# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 06:13:00 2016

@author: nataliabielczyk
"""


# Load the packages:
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io 
import xlsxwriter

#open the data:
data = scipy.io.loadmat('/Users/Kasia/Documents/WORK/Quinpirole/Python_analysis/alldata_rats.mat')
trials = data['trials']

#create the notebook:
workbook = xlsxwriter.Workbook('wyniki_kasia.xlsx')

#zone labels:
zones=['AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA']
zone_numbers=[1,5,8,14,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,6,7,9,2,3,4]

#first worksheet with intro:
read_this = workbook.add_worksheet('read_this')
read_this.set_column('A:A', 100)
read_this.write(1,0,'Data from Utrecht 2013-2014') 
read_this.write(2,0,'12 injections of Quinpirole or the saline (control) followed by open field test of 30min') 
read_this.write(3,0,'Odd numbers= qnp') 
read_this.write(4,0,'Even numbers= ctr') 
read_this.write(5,0,'At 1st, 10th and 12th test day, animals were scaned.') 
read_this.write(6,0,'Behavioural data fromQ1, Q10 and Q12') 
read_this.write(7,0,'Frequency= number of visit in given location/ zone in the open field') 
read_this.write(8,0,'Velocity= velocity during 30 min of the test') 
read_this.write(9,0,'Distance moved= distance moved during 30min of the test') 
read_this.write(10,0,'Return time= time necessary to come back to the given location/zone, counted from the moment when the animal left the zone till it cames back to the same zone') 
read_this.write(11,0,'Home base= prefered location/zone during 30min of the test, the most frequently visited, shortest return time') 
read_this.write(12,0,'number of zones visited= total number of zones visited between two consecutive visits to the one location/zone.') 
read_this.write(13,0,'min duration= min time spent in the given zone during one viist') 
read_this.write(14,0,'max duration= max time spent in the given  zone during one visit') 
read_this.write(15,0,'total duration= total time spent in one zone during the trial (30min)') 

read_this.write(18,0,'Open field- 160x160x 60cm (lxdxh):') 
read_this.write(19,0,'25 locations/ zones, each of 40x40 cm') 
read_this.write(20,0,'border locations cover 20 cm beyond the open field, necessary to detect rats head point ') 
read_this.write(21,0,'4 objects of 8x8x8cm : 2 white and 2 black') 

read_this.write(24,0,'Behaviour tests (open field) from Szechtman et al.. 1998') 
read_this.write(25,0,'Dvorkin et al., 2006, 2008, 2010') 

read_this.write(27,0,'Note: Trial ID- info necessary for researcher performing behavioural analysis with Ethovision') 


freq = workbook.add_worksheet('Frequency')
freq.write(2,0,'Zone')
freq.write(0,2,'nbr of injections')
freq.write(1,2,'rat_id')
freq.write(2,2,'trial')
for k in range(25):
    freq.write(k+3,0,zones[k])
    freq.write(k+3,1,zone_numbers[k])
for i in range(data['dane'].shape[1]):
    for j in range(data['dane'].shape[2]):
        freq.write(i+3,j+3,data['dane'][0][i][j]) 
        freq.write(i+3,j+3,data['dane'][0][i][j]) 
for j in range(data['dane'].shape[2]):
    freq.write(2,j+3,trials[j]) 
    
    
min_duration = workbook.add_worksheet('min duration')
min_duration.write(2,0,'Zone')
min_duration.write(0,2,'nbr of injections')
min_duration.write(1,2,'rat_id')
min_duration.write(2,2,'trial')
for k in range(25):
    min_duration.write(k+3,0,zones[k])
    min_duration.write(k+3,1,zone_numbers[k])
for i in range(data['dane'].shape[1]):
    for j in range(data['dane'].shape[2]):
        min_duration.write(i+3,j+3,data['dane'][1][i][j]) 
        min_duration.write(i+3,j+3,data['dane'][1][i][j])     
for j in range(data['dane'].shape[2]):
    min_duration.write(2,j+3,trials[j]) 
    

max_duration = workbook.add_worksheet('max duration')
max_duration.write(2,0,'Zone')
max_duration.write(0,2,'nbr of injections')
max_duration.write(1,2,'rat_id')
max_duration.write(2,2,'trial')
for k in range(25):
    max_duration.write(k+3,0,zones[k])
    max_duration.write(k+3,1,zone_numbers[k])
for i in range(data['dane'].shape[1]):
    for j in range(data['dane'].shape[2]):
        max_duration.write(i+3,j+3,data['dane'][2][i][j]) 
        max_duration.write(i+3,j+3,data['dane'][2][i][j]) 
for j in range(data['dane'].shape[2]):
    max_duration.write(2,j+3,trials[j]) 
    
        
total_duration = workbook.add_worksheet('total duration')
total_duration.write(2,0,'Zone')
total_duration.write(0,2,'nbr of injections')
total_duration.write(1,2,'rat_id')
total_duration.write(2,2,'trial')
for k in range(25):
    total_duration.write(k+3,0,zones[k])
    total_duration.write(k+3,1,zone_numbers[k])
for i in range(data['dane'].shape[1]):
    for j in range(data['dane'].shape[2]):
        total_duration.write(i+3,j+3,data['dane'][3][i][j]) 
        total_duration.write(i+3,j+3,data['dane'][3][i][j]) 
for j in range(data['dane'].shape[2]):
    total_duration.write(2,j+3,trials[j]) 
    
workbook.close()