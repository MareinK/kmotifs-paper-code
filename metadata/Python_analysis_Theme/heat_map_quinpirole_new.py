from xlrd import open_workbook, XL_CELL_TEXT
import numpy as np
import matplotlib as plt
import scipy as sci
import math
import scipy.io
import pylab
import os
from matplotlib.patches import Rectangle

#create new output folders if necessary:
foldername1 = 'heatmaps_jet'
if not os.path.exists(foldername1):
    os.makedirs(foldername1)
foldername2 = 'heatmaps_PiYG'
if not os.path.exists(foldername2):
    os.makedirs(foldername2)
foldername3 = 'heatmaps_Blues'
if not os.path.exists(foldername3):
    os.makedirs(foldername3)
foldername4 = 'heatmaps_spectral'
if not os.path.exists(foldername4):
    os.makedirs(foldername4)    
    
#upload the data for the plot:
book = open_workbook('frequency.xlsx')
data_sheet = book.sheet_by_index(0) #open first sheet

#create heat map matrices for every row:
Nheatmaps=data_sheet.nrows-1
mydict = {}
for i in range(Nheatmaps):
    mydict['heat_map_' + str(i+1)] = np.zeros((5, 5))
    
#find maximum value to normalize the colorbars:    
maximum = 0
for i in range(data_sheet.nrows-1):
    for j in range(data_sheet.ncols-1):
        maximum = max(maximum, data_sheet.cell_value(i+1,j+1))

b=np.zeros((5,5));
b[0][0]=22
b[0][1]=23
b[0][2]=24
b[0][3]=25
b[0][4]=10
b[1][0]=21
b[1][1]=8
b[1][2]=9
b[1][3]=2
b[1][4]=11
b[2][0]=20
b[2][1]=7
b[2][2]=1
b[2][3]=3
b[2][4]=12
b[3][0]=19
b[3][1]=6
b[3][2]=5
b[3][3]=4
b[3][4]=13
b[4][0]=18
b[4][1]=17
b[4][2]=16
b[4][3]=15
b[4][4]=14


#fill in the matrices and plot heat maps:
for i in range(Nheatmaps):
    print i
    a = mydict['heat_map_' + str(i+1)]
    a[0][0] = data_sheet.cell_value(i+1,22)
    a[0][1] = data_sheet.cell_value(i+1,23)
    a[0][2] = data_sheet.cell_value(i+1,24)
    a[0][3] = data_sheet.cell_value(i+1,25)
    a[0][4] = data_sheet.cell_value(i+1,10)
    a[1][0] = data_sheet.cell_value(i+1,21)
    a[1][1] = data_sheet.cell_value(i+1,8)
    a[1][2] = data_sheet.cell_value(i+1,9)
    a[1][3] = data_sheet.cell_value(i+1,2)
    a[1][4] = data_sheet.cell_value(i+1,11)
    a[2][0] = data_sheet.cell_value(i+1,20)
    a[2][1] = data_sheet.cell_value(i+1,7)
    a[2][2] = data_sheet.cell_value(i+1,1)
    a[2][3] = data_sheet.cell_value(i+1,3)
    a[2][4] = data_sheet.cell_value(i+1,12)
    a[3][0] = data_sheet.cell_value(i+1,19)
    a[3][1] = data_sheet.cell_value(i+1,6)
    a[3][2] = data_sheet.cell_value(i+1,5)
    a[3][3] = data_sheet.cell_value(i+1,4)
    a[3][4] = data_sheet.cell_value(i+1,13)
    a[4][0] = data_sheet.cell_value(i+1,18)
    a[4][1] = data_sheet.cell_value(i+1,17)
    a[4][2] = data_sheet.cell_value(i+1,16)
    a[4][3] = data_sheet.cell_value(i+1,15)
    a[4][4] = data_sheet.cell_value(i+1,14)

    #norm1 = plt.colors.Normalize(vmin=0,vmax=maximum/4) 
    pylab.figure()
    cmap = pylab.cm.jet
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    pylab.title(str(data_sheet.cell_value(i+1,0)))
    for ind1 in range(5):
        for ind2 in range(5):
            pylab.text(ind1, ind2, int(b[ind1][ind2]), va='center', ha='center')
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heatmaps_jet/" + str(data_sheet.cell_value(i+1, 0)) + ".png")
    pylab.show()
    
    pylab.figure()
    cmap = pylab.cm.PiYG
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    pylab.title(str(data_sheet.cell_value(i+1,0)))
    for ind1 in range(5):
        for ind2 in range(5):
            pylab.text(ind1, ind2, int(b[ind1][ind2]), va='center', ha='center')
    #im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heatmaps_PiYG/" + str(data_sheet.cell_value(i+1, 0)) + ".png")
    pylab.show()

    pylab.figure()
    cmap = pylab.cm.Blues
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    pylab.title(str(data_sheet.cell_value(i+1,0)))
    for ind1 in range(5):
        for ind2 in range(5):
            pylab.text(ind1, ind2, int(b[ind1][ind2]), va='center', ha='center')
    #im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heatmaps_Blues/" + str(data_sheet.cell_value(i+1, 0)) + ".png")
    pylab.show()
    
    pylab.figure()
    cmap = pylab.cm.spectral
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    pylab.title(str(data_sheet.cell_value(i+1,0)))
    for ind1 in range(5):
        for ind2 in range(5):
            pylab.text(ind1, ind2, int(b[ind1][ind2]), va='center', ha='center')
    #im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heatmaps_spectral/" + str(data_sheet.cell_value(i+1, 0)) + ".png")
    pylab.show()

