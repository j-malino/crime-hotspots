import geopandas as gpd
import matplotlib.pyplot as plt
import os
import pandas as pd
import fiona

def shpFileReader(directory, isMAC = True):
    #create an empty geom dataframes
    crimeData_geom = gpd.GeoDataFrame(columns=['CATEGORY', 'CALL_GROUP', 'final_case', 
                                               'CASE_DESC', 'occ_date', 'x_coordinate', 'y_coordinate', 
                                               'census_tract', 'geometry'], geometry='geometry')

    # if we are working on a pc, chage the addtional file path / to \
    addDir = 'CIS635/Geo_Data'
    if isMAC == False:
        addDir = 'CIS635\Geo_Data'

    
    for dirpath, dirnames, filenames in os.walk(directory + 'CIS635/Geo_Data'):
        for filename in filenames:
            if filename.endswith('.shp'):
                with fiona.open(dirpath + '/' + filename) as shp:
                    temp_file = gpd.read_file(shp)
                    #temp_file = gpd.read_file(dirpath + '/' + filename, engine="pyogrio")
                    crimeData_geom = crimeData_geom.merge(temp_file, how = 'outer')

    return crimeData_geom


def shpFile_brute_MAC(fileName, isMAC = True):
    slash = '/'
    if isMAC == False:
        slash = '\\'

    #2012
    #SHP_MAR01_DEC31_2012 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2012' + slash + 'NIJ2012_MAR01_DEC31.shp')

    #2013
    #SHP_JAN01_DEC31_2013 = gpd.read_file(fileName + r''CIS635' + slash + 'Geo_Data' + slash + '2013' + slash + 'NIJ2013_JAN01_DEC31.shp')

    #2014
    #SHP_JAN01_DEC31_2014 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2014' + slash + 'NIJ2014_JAN01_DEC31.shp')

    #2015
    #SHP_JAN01_DEC31_2015 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2015' + slash + 'NIJ2015_JAN01_DEC31.shp')

    #2016 -JAN-JUL, AUG, SEP, OCT, NOV, DEC
    #SHP_JAN01_JUL31_2016 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2016' + slash + 'NIJ2016_JAN01_JUL31.shp')

    #SHP_AUG01_AUG31_2016 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2016' + slash + 'NIJ2016_AUG01_AUG31.shp')

    #SHP_SEP01_SEP30_2016 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2016' + slash + 'NIJ2016_SEP01_SEP30.shp')

    #SHP_OCT01_OCT31_2016 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2016' + slash + 'NIJ2016_OCT01_OCT31.shp')

    #SHP_NOV01_NOV30_2016 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2016' + slash + 'NIJ2016_NOV01_NOV30.shp')

    #SHP_DEC01_DEC31_2016 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2016' + slash + 'NIJ2016_DEC01_DEC31.shp')

    #2017 -JAN, FEB01-FEB14, FEB15-FEB21, FEB22-FEB26, FEB27, FEB28, MAR-MAY
    SHP_JAN01_JAN31_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_JAN01_JAN31.shp')

    SHP_FEB01_FEB14_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_FEB01_FEB14.shp')

    SHP_FEB15_FEB21_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_FEB15_FEB21.shp')

    SHP_FEB22_FEB26_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_FEB22_FEB26.shp')

    SHP_FEB27_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_FEB27.shp')

    SHP_FEB28_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_FEB28.shp')

    SHP_MAR01_MAY31_2017 = gpd.read_file(fileName + r'CIS635' + slash + 'Geo_Data' + slash + '2017' + slash + 'NIJ2017_MAR01_MAY31.shp')

    #LIST_SHP_FILES = ['SHP_MAR01_DEC31_2012','SHP_JAN01_DEC31_2013','SHP_JAN01_DEC31_2014','SHP_JAN01_DEC31_2015','SHP_JAN01_JUL31_2016','SHP_AUG01_AUG31_2016','SHP_SEP01_SEP30_2016','SHP_OCT01_OCT31_2016','SHP_NOV01_NOV30_2016','SHP_DEC01_DEC31_2016','SHP_JAN01_JAN31_2017','SHP_FEB01_FEB14_2017','SHP_FEB15_FEB21_2017','SHP_FEB22_FEB26_2017','SHP_FEB27_2017','SHP_FEB28_2017','SHP_MAR01_MAY31_2017']

    print("files read")

    temp_list = [SHP_JAN01_JAN31_2017, SHP_FEB01_FEB14_2017, SHP_FEB15_FEB21_2017, 
                 SHP_FEB22_FEB26_2017, SHP_FEB27_2017, SHP_FEB28_2017, SHP_MAR01_MAY31_2017]
    
    crimeData_geom = gpd.GeoDataFrame(columns=['CATEGORY', 'CALL_GROUP', 'final_case', 
                                               'CASE_DESC', 'occ_date', 'x_coordinate', 'y_coordinate', 
                                               'census_tract', 'geometry'], geometry='geometry')
    


    
    '''
    Loops through list of geo-dataframes
    if we are on the first eleemnt in our list, set that as our first dataframe (no need to merge)
    if we are not on the first element, merge the current geo dataframe with the running geo dataframe
    '''
    index = 0
    for tempData in temp_list:
        if index != 0:
            crimeData_geom = crimeData_geom.merge(tempData, how = 'outer')
        else:
            crimeData_geom = temp_list[0]
        index += 1

    return crimeData_geom
    

def shpFile_brute_PC(directory = ""):
    #2012
    SHP_MAR01_DEC31_2012 = gpd.read_file(r'CIS635\Geo_Data\2012\NIJ2012_JAN01_DEC31.shp')

    #2013
    SHP_JAN01_DEC31_2013 = gpd.read_file(r'CIS635\Geo_Data\2013\NIJ2013_JAN01_DEC31.shp')

    #2014
    SHP_JAN01_DEC31_2014 = gpd.read_file(r'CIS635\Geo_Data\2014\NIJ2014_JAN01_DEC31.shp')

    #2015
    SHP_JAN01_DEC31_2015 = gpd.read_file(r'CIS635\Geo_Data\2015\NIJ2015_JAN01_DEC31.shp')

    #2016 -JAN-JUL, AUG, SEP, OCT, NOV, DEC
    SHP_JAN01_JUL31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_JAN01_JUL31.shp')

    SHP_AUG01_AUG31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_AUG01_AUG31.shp')

    SHP_SEP01_SEP30_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_SEP01_SEP30.shp')

    SHP_OCT01_OCT31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_OCT01_OCT31.shp')

    SHP_NOV01_NOV30_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_NOV01_NOV30.shp')

    SHP_DEC01_DEC31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_DEC01_DEC31.shp')

    #2017 -JAN, FEB01-FEB14, FEB15-FEB21, FEB22-FEB26, FEB27, FEB28, MAR-MAY
    SHP_JAN01_JAN31_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_JAN01_JAN31.shp')

    SHP_FEB01_FEB14_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB01_FEB14.shp')

    SHP_FEB15_FEB21_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB15_FEB21.shp')

    SHP_FEB22_FEB26_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB22_FEB26.shp')

    SHP_FEB27_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB27.shp')

    SHP_FEB28_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB28.shp')

    SHP_MAR01_MAY31_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_MAR01_MAY31.shp')

    LIST_SHP_FILES = ['SHP_MAR01_DEC31_2012','SHP_JAN01_DEC31_2013','SHP_JAN01_DEC31_2014','SHP_JAN01_DEC31_2015','SHP_JAN01_JUL31_2016','SHP_AUG01_AUG31_2016','SHP_SEP01_SEP30_2016','SHP_OCT01_OCT31_2016','SHP_NOV01_NOV30_2016','SHP_DEC01_DEC31_2016','SHP_JAN01_JAN31_2017','SHP_FEB01_FEB14_2017','SHP_FEB15_FEB21_2017','SHP_FEB22_FEB26_2017','SHP_FEB27_2017','SHP_FEB28_2017','SHP_MAR01_MAY31_2017']

def cleaningGEO(geoDF):
    crimeGeoDf = gpd.GeoDataFrame(geoDF)
    #cleaningDF = pd.DatFrame(crimeGeoDf)
    print("starting clean")
    #crimeGeoDf = crimeGeoDf.dropna(inplace=True)
    print("end of cleaning")
    return crimeGeoDf


def plotGeo(geoDF):
    crimeGeoDf = gpd.GeoDataFrame(geoDF)
    crimeGeoDf.plot(figsize=(10,6))
    plt.show()