# code for loading and saving xarray datasets in a general way.

import itertools
import os

import xarray as xr

def save(ds, name, overwrite=False):
    path = f'../datasets/{name}.nc'
    if os.path.isfile(path) and not overwrite:
        raise Exception('dataset already exists (use overwrite=True)')
    variables = itertools.chain(ds.coords, ds.data_vars)
    encoding = {var: {'zlib': True} for var in variables}
    ds.to_netcdf(path, encoding=encoding, engine='h5netcdf')

def load(name):
    path = f'../datasets/{name}.nc'
    return  xr.open_dataset(path, engine='h5netcdf')
