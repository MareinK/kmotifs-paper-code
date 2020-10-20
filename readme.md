# Marein Könings Bachelor Thesis Code Repository

This repository contains a (somewhat cleaned-up version of) the code that I used to research and create the results and figures in my Bachelor Thesis.

Although some straight executable or importable Python code files (.py) exist in this repository, a lot of the work was done in a less structured fashion, using Jupyter Notebooks (.ipynb). These notebooks contain cells that can be executed in any order, which facilitates nonlinear, iterative workflows. But this makes them less useful for examination afterwards. As such, the code in this repository might be difficult to understand, although comments have been added at the top of each .py/.ipynb file to explain its general purpose. Note also that due to changes in folder organisation throughout the project, some code that is dependent on filepaths will no longer run.

## Folders

The purpose of each folder will be briefly explained:

- data - The original Excel data sheets containing the Ethovision output
- data_clean - Selected original data converted to (gzipped) .csv format
- data_final - Futher preparation steps applied to cleaned data
- datasets - Different variants of datasets saved using `xarray` format (the format the was ultimately used in the methods)
- literature - A small selection of literature research from the start of the project, including research into biomarker frequency (for data augmentation)
- metadata - Information that was supplied with the original datasets
- plots - Images and movies depicting the data
- scripts - All .py and .ipynb files
- thesis - The LaTeX files and images used to create the thesis document, and some specific Python files.

## Collaboration

Note that some script files and their output was created in collaboration with Jesse Zwamborn, in particular those pertaining to the preparation and visualisation of the data and the evaluation of classifiers.

## Interesting files

These files are probably of particular interest to my own project:

- sax.ipynb (although it is extremely messy)
- sax.py
- seq.py

# xarray

Heavy use was made of the [`xarray` Python package](http://xarray.pydata.org/), which is an extension of `numpy` and `pandas`, and greatly facilitates the manipulation of higher-dimensional labeled data.

## k-motifs package

In order to create a more reusable, structured code, an attempt was made at one point to create a package implementing the k-motifs algorithm, as no good package exists yet for Python. However there was not enough time to finish this package. The beginnings can be found in the folder `scripts/kmotif` (duplicating some files from the `scripts` folder).

# Implementations of algorithms

The k-motifs package primarily implements the SAX and Sequitur algorithms, since these are the basis of the k-motifs algorithm. Individual implementations of these algorithms do already exist for Python, but they were not suitable for the current project. In particular, the existing implementations are not sufficiently general.

The existing implementations of SAX do not allow arbitrary values of alpha, but instead limit alpha to some pre-defined values with corresponding percentiles of the normal distribution. My implementation dynamically calculates the percentiles based on the arbitrary value of alpha.

Additionally, the existing SAX implementations normalise the input data and create bins from the unit normal distribution, while I wanted to forego normalising the input data and instead create bins from a normal distribution based on the input data.

Existing Sequitur implementations do not allow the input stream to consist of letters only ('a b b d c'). This would require the conversion of SAX bin indices ('0 2 1 2 3'), and particular two-dimensional SAX results ('(0,1) (0,2) (1,2) (2,2) (1,2)') to be converted to letters. This makes the output of Sequitur more difficult to interpret and also limits the amount of symbols to the amount of letters/characters. For these reasons a new implmentation of Sequitur was made that allows for arbitrary symbols in the input stream.

# Large files

The repository contains a large number of large files, containing (different versions of) the experimental data. We use [GIT LFS](https://www.atlassian.com/git/tutorials/git-lfs) to prevent problems with large files in the GIT repository.
