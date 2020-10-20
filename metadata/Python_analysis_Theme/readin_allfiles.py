from xlrd import open_workbook, XL_CELL_TEXT
import xlwt
import numpy as np
import matplotlib as plt
import scipy as sci
import math
import scipy.io
from os import listdir
from os.path import isfile, join
# do instalowania paczek: sciagasz na dysk i w terminalu:
# conda install <nazwa>

#upload the data for the plot:
mypath = '/Users/Kasia/Desktop/results_utrecht_august_2016/results/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlydata = []
trials = []

for i in range(len(onlyfiles)):
    if onlyfiles[i][0:5] == 'Track':
        onlydata.append(onlyfiles[i])
        trials.append(onlyfiles[i][-46:-43])
        
Nfiles=len(onlydata)

# stworz tablice z danymi:
dane = np.empty((4,25,Nfiles))

for k in range(len(onlydata)):
    print k+1
    book = open_workbook(mypath + onlydata[k])
    data_sheet = book.sheet_by_index(6) #open first sheet

    for j in range(25):
        dane[0,j,k]=data_sheet.cell_value(j+11,3)
        dane[1,j,k]=data_sheet.cell_value(j+11,4)
        dane[2,j,k]=data_sheet.cell_value(j+11,5)
        dane[3,j,k]=data_sheet.cell_value(j+11,7)

scipy.io.savemat('alldata_rats.mat', dict(dane=dane,trials=trials))
#saving:
#book = xlwt.Workbook(encoding="utf-8")
#sheet1 = book.add_sheet("Frequency")
#for 
#sheet1.write(0, 0, "Display")
