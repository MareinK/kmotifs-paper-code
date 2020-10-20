from xlrd import open_workbook, XL_CELL_TEXT
import xlwt
import numpy as np
import matplotlib as plt
import scipy as sci
import math
import scipy.io
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
# do instalowania paczek: sciagasz na dysk i w terminalu:
# conda install <nazwa>


version='2016' #or 'utrecht' or '2013' or '2012'
#given path to the data:
mypath = '/Users/nataliabielczyk/Desktop/RAT/data_2016/' 
#give path to the output folder:
mypath1 = '/Users/nataliabielczyk/Desktop/RAT/Python_analysis_Theme/output_2016/'#'/Users/Kasia/Documents/WORK/RAT/output_txt/'

#change sequence depending on the version:
if version=='2016': #Kasia's laptop
    sequence = [1,5,8,14,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,6,7,9,2,3,4]
if version=='utrecht': #Kasia's external disc
    sequence = [18,19,20,21,22,23,24,25,10,17,16,15,14,6,7,8,5,1,9,4,3,2,13,12,11] 
if version=='2013': #Kasia's external disc
    sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
if version=='2012': #Kasia's external disc
    sequence = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,2,3,4,5,6,7,8,9,1]
    
# -------------------------------------------
# the rest is the same:  
    
#read in the data:
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlydata = []
trials = []
for i in range(len(onlyfiles)):
    if onlyfiles[i][0:5] == 'Track':
        onlydata.append(onlyfiles[i])  
        trials.append(onlyfiles[i][-46:-43])     
Nfiles=len(onlydata)  

for k in range(len(onlydata)):

    print (k+1)   
    print onlydata[k]
    book = open_workbook(mypath + onlydata[k])
    data_sheet = book.sheet_by_index(2)
    first_col=np.zeros((data_sheet.nrows,1))
    for ind in range(0, data_sheet.nrows):
        if data_sheet.cell_value(ind, 0)=='Trial time':
            index=ind

    #find fields with 'Start':
    starts0=np.zeros((data_sheet.nrows-index-2,1))
    for ind in range(data_sheet.nrows-index-2):
        for ind2 in range(data_sheet.ncols):
            if data_sheet.cell_value(ind+index+1,ind2)=='Start':
                starts0[ind]=ind2-1
                
    #change the sequence:
    starts=np.zeros((data_sheet.nrows-index-2,1))
    for ind in range(data_sheet.nrows-index-2):
        starts[ind]=sequence[int(starts0[ind]-1)]
        
    #take the data from the column below 'Trial time':
    data=np.zeros((data_sheet.nrows-index-2,3))
    for ind in range(data_sheet.nrows-index-2): # cut down the last row because it does not contain 'Start'
        #recording time and make integers by multiplying by 100:
        data[ind,0]=int(trials[k])
        data[ind,1]=int(float(data_sheet.cell_value(ind+index+1, 1))*100.0)
        data[ind,2]=int(starts[ind])
    
    filename=trials[k]+'.txt'
    np.savetxt(mypath1 + '/' + filename, data, delimiter=' ', fmt='%u')