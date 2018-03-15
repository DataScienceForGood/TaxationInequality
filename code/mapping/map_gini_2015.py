import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

from read_data import *

# - Read map and 2015 tax data
gdfMap = read_WV_map()
dfIncome = read_2015_income()
dfAssets = read_2015_assets()

(dfMap_WVid_name, dfMapWVid_geoID, dfMapICid, dfMapACid) = read_2015_mappings()

dfTax2015 = pd.read_csv('../../data/data2015.csv')
gpdMapTax = pd.merge(gdfMap, dfTax2015, left_on = 'OBJECTID', right_on = 'wohnviertel_id')
gpdMapTax.plot(column = 'reinverm_gini')
