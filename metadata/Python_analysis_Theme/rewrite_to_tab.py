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

#give path to the script:
mypath = '/Users/nataliabielczyk/Desktop/RAT/Python_analysis_Theme/'
#the folder with output files you want to process:
folder='output_2016' #or 'output_utrecht' or 'output_2013' or 'output_2012'


#create new output folder if necessary:
foldername = mypath+folder+'_themefriendly'
if not os.path.exists(foldername):
    os.makedirs(foldername)

onlyfiles = [f for f in listdir(mypath+folder) if isfile(join(mypath+folder, f))]
onlydata = []
for i in range(len(onlyfiles)):
    if onlyfiles[i][-3:] == 'txt':
        list1=['trial id']
        list2=['time']
        list3=['event']
        with open(folder+'/'+onlyfiles[i]) as f:
            data = f.readlines()
            for ind in range(len(data)):
                string=data[ind]
                a=string.split(" ")
                list1.append(a[0])
                list2.append(a[1])
                list3.append(a[2][:-1])

        # create output file:
        name=foldername+'/'+onlyfiles[i]

        with open (name,'a') as proc_seqf:
            for i1, i2, i3 in zip(list1, list2, list3):
                proc_seqf.write("{}\t{}\t{}\n".format(i1,i2,i3))




#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#onlydata = []
#trials = []
#for i in range(len(onlyfiles)):
#    if onlyfiles[i][0:5] == 'Track':
#        onlydata.append(onlyfiles[i])  
#        trials.append(onlyfiles[i][-46:-43])     
#Nfiles=len(onlydata)  
#
