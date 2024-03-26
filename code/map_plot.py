""" import numpy as np 
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
 """
#import json
#import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
import folium
from branca.utilities import split_six
from folium.plugins import FastMarkerCluster, HeatMap

'''
https://focaalvarez.medium.com/mapping-the-uk-and-navigating-the-post-code-maze-4898e758b82f
https://medium.com/@patohara60/interactive-mapping-in-python-with-uk-census-data-6e571c60ff4
https://stackoverflow.com/questions/46775667/plotting-uk-districts-postcode-areas-and-regions
'''

#https://sdgdata.gov.uk/sdg-data/geojson-output-regions.html
uk = 'https://sdgdata.gov.uk/sdg-data/en/geojson/regions/indicator_8-10-1.geojson'

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    plotMap(df)

def plotMap(df):
    m = folium.Map(location=[55,4], zoom_start=5)
    folium.GeoJson(uk).add_to(m)
    """ folium.Choropleth( geo_data = state_geo,
                        data = df,
                        columns=["Region", "Population Base"]) """
    #folium.LayerControl().add_to(map)
    m.show_in_browser()

if __name__ == "__main__":
    main()