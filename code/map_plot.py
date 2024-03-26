
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
import folium
from branca.utilities import split_six
from folium.plugins import FastMarkerCluster, HeatMap

from stats import getGroupTable
from census_microdata_2011 import dataset

'''
https://focaalvarez.medium.com/mapping-the-uk-and-navigating-the-post-code-maze-4898e758b82f
https://medium.com/@patohara60/interactive-mapping-in-python-with-uk-census-data-6e571c60ff4
https://stackoverflow.com/questions/46775667/plotting-uk-districts-postcode-areas-and-regions
https://realpython.com/python-folium-web-maps-from-data/ THIS IS MAIN SOURCE
https://stackoverflow.com/questions/54595931/show-different-pop-ups-for-different-polygons-in-a-geojson-folium-python-ma 
'''

#https://sdgdata.gov.uk/sdg-data/geojson-output-regions.html
eng = 'https://sdgdata.gov.uk/sdg-data/en/geojson/regions/indicator_8-10-1.geojson'
#https://findthatpostcode.uk/areas/W92000004.html
wales = 'https://findthatpostcode.uk/areas/W92000004.geojson'

ftp_url = 'https://findthatpostcode.uk/areas/'

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    getTableHtml(df, "E12000001", "Marital Status")
    plotMap(df, "Marital Status")

def plotMap(df, col):
    m = folium.Map(location=[54.38, -2.7], zoom_start=5)
    for reg in dataset.get_column("Region").values:
        data = ftp_url + reg + ".geojson"
        f = folium.Choropleth(geo_data = data,
                                data = df,
                                columns = ["Region",col],
                                fill_color = "RdYlGn_r",
                                fill_opacity=.8,
                                key_on="feature.properties.code")
        folium.GeoJsonTooltip(["code"], aliases=[getTableHtml(df,reg,col)]).add_to(f.geojson)
        f.add_to(m)
    """ for key in m._children:
        if key.startswith('color_map'):
            del(m._children[key]) """
    m.show_in_browser()

def getTableHtml(df, region, col):
    table = getGroupTable(df, "Region", col) # get unique counts of col
    t = table[table["Region"].values == region] # filter to just specified region
    t =t.drop(labels="Region",axis=1) # remove region column
    return t.to_html(index=False) # return as html w/ no indices

if __name__ == "__main__":
    main()