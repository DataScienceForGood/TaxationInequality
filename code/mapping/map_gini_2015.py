import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

gpdMap = gpd.read_file('../../data/WE_StatWohneinteilungen/Wohnviertel.shp')
gpdMap['area'] = gpdMap.area
gpdMap.plot(column = 'OBJECTID')

dfTax2015 = pd.read_csv('../../data/data2015.csv')

gpdMapTax = pd.merge(gpdMap, dfTax2015, left_on = 'OBJECTID', right_on = 'wohnviertel_id')

gpdMapTax.plot(column = 'reinverm_gini')