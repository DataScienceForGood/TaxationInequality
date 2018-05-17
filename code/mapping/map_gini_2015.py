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

dfTax2015 = pd.read_csv('../../data/data.csv')
gpdMapTax = pd.merge(gdfMap, dfTax2015, left_on = 'OBJECTID', right_on = 'wohnviertel_id')
gpdMapTax.plot(column = 'reinverm_gini')

# - Get unique Wohnviertel IDs
vnWVIDs = pd.unique(dfIncome['wohnviertel_id'])

# - Get total income tax for each wohnviertel
def find_WV(wv_id):
    return dfIncome.wohnviertel_id.map(lambda i: i == wv_id)

def find_IC(ic_id):
    return dfIncome.incomeclass_id.map(lambda i: i == ic_id)

vfWVTotalIncomeTax = [sum(dfIncome.loc[find_WV(id), 'total_income_tax'])
                      for id in vnWVIDs]

# - Get percentage of total income tax for lowest income bracket
def find_WV_IC(wv_id, ic_id):
    return find_WV(wv_id) & find_IC(ic_id)

vfPrcIncomeTaxLowestBracket = [
    np.asscalar(dfIncome.loc[find_WV_IC(wv, 1), 'total_income_tax'] / tot) \
    for wv, tot in zip(vnWVIDs, vfWVTotalIncomeTax)
    ]

vfPrcIncomeTaxHighestBracket = [
    np.asscalar(dfIncome.loc[find_WV_IC(wv, 5), 'total_income_tax'] / tot) \
    for wv, tot in zip(vnWVIDs, vfWVTotalIncomeTax)
    ]

vnNumDeclarationsBrackets = [
    np.sum(dfIncome.loc[find_IC(ic), 'num_declarations']) for ic in range(1, 6)
    ]

dfPrcIncomeTax = pd.DataFrame({'wohnviertel_id': vnWVIDs,
                               'prop_inc_tax_lowest': np.asarray(vfPrcIncomeTaxLowestBracket) * 100,
                               'prop_inc_tax_highest': np.asarray(vfPrcIncomeTaxHighestBracket) * 100})

dfPrcIncomeTax = pd.merge(dfPrcIncomeTax, dfMapWVid_geoID,
                          on = 'wohnviertel_id')

gdfMapTax = pd.merge(gdfMap, dfPrcIncomeTax,
                     left_on = 'OBJECTID', right_on = 'geo_wohnviertel_id')

# - Plot maps of proportion of income tax paid by respective brackets
plt.figure()
ax = gdfMapTax.plot(column = 'prop_inc_tax_lowest', vmin = 0, vmax = 2)
fig = ax.get_figure()
cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=2))
# fake up the array of the scalar mappable. Urgh...
sm._A = []
fig.colorbar(sm, cax=cax)
plt.show()


plt.figure()
ax = gdfMapTax.plot(column = 'prop_inc_tax_highest', vmin = 0, vmax = 100)
fig = ax.get_figure()
cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=100))
# fake up the array of the scalar mappable. Urgh...
sm._A = []
fig.colorbar(sm, cax=cax)
plt.show()