FOR ASSIGNMNET 1 

I used Energy Data from the following website:

"https://data.cityofnewyork.us/Environment/Energy-and-Water-Data-Disclosure-for-Local-Law-84-/rgfe-8y2z" 

I exported the data as a .csv file and named it "Energy_and_Water_Data_Disclosure_for_Local_Law_84__2013_.csv"

I used Pluto Data set to get Building Unit Information. 

I downlaoded the Manhattan MapPLUTO data as a zip file and extracted the .shp file named "MNMapPLUTO.shp"

I used the following packages

import geopandas as gp
import pandas as pd
import os
import csv
import pylab as pl
from pandas.tools.plotting import scatter_matrix
import statsmodels.api as sm
import statsmodels.formula.api as smf

All packages except geopandas was installed in Python. I had to install geopandas before beginning this assignment.

I tried to make my file reproducible by setting an environmental variable for my file paths as PUI2015 but I failed to do so.

FOR ASSIGNMNET 2

I read all the files from Dr.Federica's link, so this notebook should be fully reproducible and can be run without installing/donwloading any pacakges or file. 