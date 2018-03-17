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

# - Get unique Wohnviertel IDs
vnWVIDs = pd.unique(dfIncome['wohnviertel_id'])

# - Get total income tax for each wohnviertel
def find_WV(wv_id):
    return dfIncome.wohnviertel_id.map(lambda i: i == wv_id)

vfWVTotalIncomeTax = [sum(dfIncome.loc[find_WV(id), 'total_income_tax'])
                      for id in vnWVIDs]

# - Get percentage of total income tax for lowest income bracket
def find_WV_IC(wv_id, ic_id):
    return find_WV(wv_id) & \
           dfIncome.incomeclass_id.map(lambda i: i == ic_id)

vfPrcIncomeTaxLowestBracket = [
    np.asscalar(dfIncome.loc[find_WV_IC(wv, 1), 'total_income_tax'] / tot) \
    for wv, tot in zip(vnWVIDs, vfWVTotalIncomeTax)
    ]

vfPrcIncomeTaxHighestBracket = [
    np.asscalar(dfIncome.loc[find_WV_IC(wv, 5), 'total_income_tax'] / tot) \
    for wv, tot in zip(vnWVIDs, vfWVTotalIncomeTax)
    ]

dfPrcIncomeTax = pd.DataFrame({'wohnviertel_id': vnWVIDs,
                               'prop_inc_tax_lowest': vfPrcIncomeTaxLowestBracket,
                               'prop_inc_tax_highest': vfPrcIncomeTaxHighestBracket})

dfPrcIncomeTax = pd.merge(dfPrcIncomeTax, dfMapWVid_geoID,
                          on = 'wohnviertel_id')

gdfMapTax = pd.merge(gdfMap, dfPrcIncomeTax,
                     left_on = 'OBJECTID', right_on = 'geo_wohnviertel_id')

# - Plot maps of proportion of income tax paid by respective brackets
gdfMapTax.plot(column = 'prop_inc_tax_lowest')
gdfMapTax.plot(column = 'prop_inc_tax_highest')