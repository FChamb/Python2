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
from folium.plugins import FastMarkerCluster, HeatMap


def main():
    #df = pd.read_csv("data/census2011-clean.csv")
    folium_map = folium.Map(location=[53,2], zoom_start=2, tiles='cartodbpositron')
    #FastMarkerCluster(data=list(zip(outdf['latitude'].values, outdf['longitude'].values))).add_to(folium_map)
    folium.LayerControl().add_to(folium_map)
    folium_map.show_in_browser()
    plotMap()

def plotMap():
    locator = Nominatim(user_agent="myGeocoder")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    point = geocode('United Kingdom')
    point2 = geocode('St. Andrews')

if __name__ == "__main__":
    main()