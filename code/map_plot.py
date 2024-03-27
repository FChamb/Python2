#!/usr/bin/env python
import pandas as pd
import folium
import os
from tabulate import tabulate

from stats import getGroupTable
from census_microdata_2011 import dataset
from basic_plots import genDistPieChart, getLegend

'''
https://focaalvarez.medium.com/mapping-the-uk-and-navigating-the-post-code-maze-4898e758b82f
https://medium.com/@patohara60/interactive-mapping-in-python-with-uk-census-data-6e571c60ff4
https://stackoverflow.com/questions/46775667/plotting-uk-districts-postcode-areas-and-regions
https://realpython.com/python-folium-web-maps-from-data/ THIS IS MAIN SOURCE
https://stackoverflow.com/questions/54595931/show-different-pop-ups-for-different-polygons-in-a-geojson-folium-python-ma 
OLD DATA - https://sdgdata.gov.uk/sdg-data/geojson-output-regions.html + https://findthatpostcode.uk/areas/W92000004.html
'''
imagesDir = "../images/maps/"
ftp_url = 'https://findthatpostcode.uk/areas/'

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    m = plotMap(df, "Economic Activity")
    m.show_in_browser()

def plotMap(df, col):
    m = folium.Map(location=[54.38, -2.7], zoom_start=5)
    for reg in dataset.get_column("Region").values:
        # query find that postcode API
        data = ftp_url + reg + ".geojson"
        f = folium.Choropleth(geo_data = data,
                                data = df,
                                columns = ["Region",col],
                                fill_color = "RdYlGn_r",
                                fill_opacity=.8,
                                key_on="feature.properties.code",
                                legend_name = "Average " + col + " By Region\n")
        # add table pop up
        folium.GeoJsonTooltip(["code"], aliases=[getTableHtml(df,reg,col)]).add_to(f.geojson)
        # remove all but one legend
        if reg != dataset.get_column("Region").values[0]:
            for key in f._children:
                if key.startswith('color_map'):
                    del(f._children[key])
        f.add_to(m)
    # add legend icon
    legend = "<br>".join(getLegend(col)) 
    folium.Marker(location = [57, -8],
                    draggable = True,
                    icon = None,
                    tooltip = folium.Tooltip(legend, permanent=True)).add_to(m)
    #m.show_in_browser() # show
    m.save(imagesDir + col.replace(' ', '-').lower() + '-map.html')
    return m

def getTableHtml(df, region, col):
    table = getGroupTable(df, "Region", col) # get unique counts of col
    t = table[table["Region"].values == region] # filter to just specified region
    t =t.drop(labels="Region",axis=1) # remove region column
    return t.to_html(index=False) # return as html w/ no indices

if __name__ == "__main__":
    os.makedirs(imagesDir, exist_ok = True)
    main()