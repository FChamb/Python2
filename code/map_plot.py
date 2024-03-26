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
https://realpython.com/python-folium-web-maps-from-data/ THIS IS MAIN SOURCE
'''

#https://sdgdata.gov.uk/sdg-data/geojson-output-regions.html
eng = 'https://sdgdata.gov.uk/sdg-data/en/geojson/regions/indicator_8-10-1.geojson'
#https://findthatpostcode.uk/areas/W92000004.html
wales = 'https://findthatpostcode.uk/areas/W92000004.geojson'

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    plotMap(df, "Health")

def plotMap(df, col): # eventually change to take any column
    # add check for column validity
    m = folium.Map(location=[55,4], zoom_start=5)
    #folium.GeoJson(wales).add_to(m)
    # remove legend from wales
    folium.Choropleth(geo_data = wales,
                      data = df,
                      columns = ["Region",col],
                      fill_color = "RdYlGn_r",
                      key_on="feature.properties.code").add_to(m)
    folium.Choropleth( geo_data = eng,
                        data = df,
                        columns=["Region", col],
                        key_on="feature.properties.geocode",
                        fill_color = "RdYlGn_r",
                        fill_opacity=.8,
                        legend_name=col+" per Region").add_to(m)
    m.show_in_browser()

if __name__ == "__main__":
    main()