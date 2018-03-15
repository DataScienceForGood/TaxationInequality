# - Import required modules
import geopandas as gpd
import pandas as pd
import os

# - Data location default
DEF_strDataDir = '../../data'
strFile_2015IncomeAssets = 'Steuern_Klassen_Wohnviertel_cleaned.xlsx'
strFile_BSWVMap = 'WE_StatWohneinteilungen/Wohnviertel.shp'

def read_2015_income(strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_2015_income - Read the 2015 income table

    :param strDataDir: Data directory location. Default: '../../data'
    :return:           pd.DataFrame dfIncome
    """

    # - Read and return Income data table
    return pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                         sheet_name = 'Income', header = 3, skip_footer = 2)


def read_2015_assets(strDataDir: str = DEF_strDataDir) -> pd.DataFrame:
    """
    read_2015_assets - Read the 2015 assets table

    :param strDataDir: Data directory location. Default: '../../data'
    :return: pd.DataFrame dfAssets
    """

    # - Read and return Assets data table
    return pd.read_excel(os.path.join(strDataDir, strFile_2015IncomeAssets),
                         sheet_name = 'Assets', header = 3, skip_footer = 2)


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


