# code used to convert selected data from raw Ethovision Excel sheets to zipped comma separated files

import os
import xlrd
import numpy as np
import pandas as pd

import colors

SHEET_NAME = 'Org.Data' # sheet containing data
HEADER_ROWS_CELL = (0,1) # cell containing number of header rows before data starts
DATA_COLS = 11 # number of columns to include in data

# merges a two-row header of a single column into a single row header for that column
def merge_headers(hs):
  if not isinstance(hs[1],str):
    return hs[0]
  else:
    return ' '.join(hs)

def convert(filepath_in,filepath_out):
  wb = xlrd.open_workbook(filepath_in,on_demand=True) # load file into xlrd workbook
  sheet = wb.sheet_by_name(SHEET_NAME) # get data sheet
  metadata_rows = int(sheet.cell(*HEADER_ROWS_CELL).value) # get number of rows before data starts
  header = [metadata_rows-2,metadata_rows-1] # construct list containing numbers of rows with data headers
  df = pd.read_excel(wb, sheetname=SHEET_NAME, header=metadata_rows-2, parse_cols=DATA_COLS, engine='xlrd', na_values='-') # convert workbook to pandas dataframe
  df.columns = pd.Index(merge_headers(hs) for hs in zip(df.columns.tolist(),df.iloc[0].values))
  df = df[1:]
  os.makedirs(os.path.dirname(filepath_out), exist_ok=True) # create directory structure
  df.to_csv(filepath_out,compression='gzip') # write dataframe as compressed comma-separated values

def convert_all(dirpath):
  for root, _, filenames in os.walk(dirpath):
    for filename in filenames:
      if filename.endswith('.xlsx'):
        filepath = os.path.join(root,filename)
        filepath_out = filepath.replace('.xlsx','.csv.gz').replace('/data/','/data_clean/')
        print(f'Processing file {filepath}')
        try:
          convert(filepath,filepath_out)
        except Exception as e:
          print(colors.r(f'Failed: {str(e)}'))

if __name__ == '__main__':
  convert_all('../data')

