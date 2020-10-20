from xlrd1 import open_workbook, XL_CELL_TEXT
import numpy as np
import matplotlib as plt
import scipy as sci
import math
import scipy.io
import pylab
from matplotlib.patches import Rectangle


#upload the data for the plot:
book = open_workbook('data_quinpirole.xlsx')
data_sheet = book.sheet_by_index(0) #open first sheet

#create heat map matrices:
mydict = {}
for i in range(6):
    mydict['heat_map_' + str(i+1)] = np.zeros((5, 5))
    
#find maximum value to normalize the colorbars:    
maximum = 0
for i in range(6):
    for j in range(25):
        maximum = max(maximum, data_sheet.cell_value(i+1,j+1))

#fill in the matrices and plot heat maps:
for i in range(6):
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

    norm1 = plt.colors.Normalize(vmin=0,vmax=maximum) 
    cmap = pylab.cm.jet
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heat_map_jet_group" + str(i+1) + ".png")
    pylab.show()
    
    cmap = pylab.cm.PiYG
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heat_map_PiYG_group" + str(i+1) + ".png")
    pylab.show()

    
    cmap = pylab.cm.Blues
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heat_map_Blues_group" + str(i+1) + ".png")
    pylab.show()

    cmap = pylab.cm.spectral
    im = pylab.imshow(a, cmap=cmap, interpolation='nearest')
    im.set_norm(norm1)
    pylab.axis('off')
    pylab.colorbar(im)
    pylab.savefig("heat_map_spectral_group" + str(i+1) + ".png")
    pylab.show()

    
pylab.show()

