# - Import required modules
import geopandas as gpd
import pandas as pd
import os
import sys
# sys._enablelegacywindowsfsencoding()

from typing import Tuple

# - Data location default
DEF_strDataDir = '../../data'
strFile_2015IncomeAssets = 'Steuern_Klassen_Wohnviertel_cleaned.xlsx'
strFile_BSWVMap = 'WE_StatWohneinteilungen/Wohnviertel.shp'

dAncillaryDataSets = {
    'PropWomenAtWork':          ('Anteil Frauen an den Beschäftigten.csv', 'PropWomenAtWork'),
    'PropGreenArea':            ('Anteil Grünfläche.csv', 'PropGreenArea'),
    'PropSwiss':                ('Anteil Schweizer an der Gesamtbevölkerung.csv', 'PropSwiss'),
    'Prop1-2RoomApartments':    ('Anteil Wohnungen mit 1 oder 2 Zimmern am Gesamtwohnungsbestand.csv', 'PropApartments'),
    'NumRobberies':             ('Anzahl Einbruch- und Einschleichdiebstähle.csv', 'NumRobberies'),
    'NumDogsPer100':            ('Anzahl Hunde pro 100 Einwohner.csv', 'NumDogs'),
    'PopPerHectare':            ('Anzahl Personen pro Hektare.csv', 'PopPerHect'),
}

def read_ancillary_data(strDataKey, strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_ancillary_data - Read an extra data set

    :param strDataKey:  string Key identifying the data set (see `dAncillaryDataSets`
    :param strDataDir:  string Data directory location. Default: '../../data'
    :return:            pd.DataFrame dfData
    """
    assert strDataKey in dAncillaryDataSets.keys(), \
        '`strDataKey` must be one of the recognised data sets'

    dfData = pd.read_csv(os.path.join(strDataDir, dAncillaryDataSets[strDataKey][0]),
                         sep = ';', decimal = ',')
    return dfData.rename(index = str,
                  columns = {
                      'Code': 'wohnviertel_id',
                      'Name': 'Wohnviertel',
                      'Wert': dAncillaryDataSets[strDataKey][1],
                  })

def read_2015_income(strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_2015_income - Read the 2015 income table

    :param strDataDir: Data directory location. Default: '../../data'
    :return:           pd.DataFrame dfIncome
    """

    # - Read and return Income data table
    return pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                         sheet_name = 'Income', header = 3, skipfooter = 2)

def read_2015_gini(strDataDir: str = DEF_strDataDir) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    read_2015_gini - Read the 2015 GINI data (income and assets)

    :param strDataDir: Data directory location. Default: '../../data'
    :return:           Tuple (pd.DataFrame dfGiniIncome, pd.DataFrame dfGiniAssets)
    """

    # - Read GINI data for income
    dfGiniIncome = pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                                 sheet_name = 'income_gini', header = 3,
                                 )

    dfGiniAssets = pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                                 sheet_name = 'assets_gini', header = 3,
                                 )

    return dfGiniIncome, dfGiniAssets

def read_2015_assets(strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_2015_assets - Read the 2015 assets table

    :param strDataDir: Data directory location. Default: '../../data'
    :return: pd.DataFrame dfAssets
    """

    # - Read and return Assets data table
    return pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                         sheet_name = 'Assets', header = 3, skipfooter = 2)

def read_2015_income_quintiles(strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_2015_income - Read the 2015 income table (quintiles)

    :param strDataDir: Data directory location. Default: '../../data'
    :return:           pd.DataFrame dfIncome
    """

    # - Read and return Income data table
    return pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                         sheet_name = 'Income_quintiles', header = 3, skipfooter = 2)


def read_2015_assets_quintiles(strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_2015_assets - Read the 2015 assets table (quintiles)

    :param strDataDir: Data directory location. Default: '../../data'
    :return: pd.DataFrame dfAssets
    """

    # - Read and return Assets data table
    return pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                         sheet_name = 'Assets_quintiles', header = 3, skipfooter = 2)

def read_2015_mappings(strDataDir: str = DEF_strDataDir) -> (pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame):
    """
    read_2015_mappings - Read the mapping tables for 2015 income and assets

    :param strDataDir: Data directory location. Default: '../../data'
    :return:           (dfMap_WVid_name, dfMapWVid_geoID, dfMapICid, dfMapACid)
                        All pd.DataFrames:
                        dfMap_WVid_name: Mapping between Wohnviertel ID and name
                        dfMapWVid_geoID: Mapping between Wohnviertel ID and GIS wohnviertel ID
                        dfMapICid: Mapping between income class ID and data about each income class
                        dfMapACid: Mapping between asset class ID and data about each asset class
    """

    # - Read mapping between Wohnviertel ID and Wohnviertel name
    dfMap_WVid_name = pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                                    sheet_name = 'mapping_wohnviertel_id', header = 2)

    # - Read mapping between Wohnviertel ID and GIS Wohnviertel ID
    dfMapWVid_geoID = pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                                    sheet_name = 'mapping_wohnviertel_geo_id', header = 2)

    # - Read mapping between Income class ID and data about each income class
    dfMapICid = pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                              sheet_name = 'mapping_incomeclass_id', header = 2)

    # - Read mapping between Asset class ID and data about each asset class
    dfMapACid = pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                              sheet_name = 'mapping_assetclass_id', header = 2)

    return dfMap_WVid_name, dfMapWVid_geoID, dfMapICid, dfMapACid


def read_WV_map(strDataDir: str = DEF_strDataDir) -> gpd.GeoDataFrame:
    """
    read_WV_map - Import GIS data for the Wohnviertel map of Basel-Stadt

    :param strDataDir: Data directory location. Default: '../../data'
    :return:           gpd.GeoDataFrame gdfBaselStadtWohnviertel
    """
    # - Read and return the Wohnviertel map
    return gpd.read_file(os.path.join(strDataDir, strFile_BSWVMap))


