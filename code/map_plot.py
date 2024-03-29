#!/usr/bin/env python
import pandas as pd
import folium
import os
import sys

from stats import getGroupTable
from census_microdata_2011 import dataset
from basic_plots import genDistPieChart, getLegend

imagesDir = "images/maps/"
ftp_url = 'https://findthatpostcode.uk/areas/' # api for obtaining geojson

def main(csvPath):
    df = pd.read_csv(csvPath)
    plotMap(df, "Age", True)
    plotMap(df, "Marital", True)

def plotMap(df, col, save):
    print("Generating region by " + col + " map...\n")
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
    if save:
        m.save(imagesDir + col.replace(' ', '-').lower() + '-map.html')
    else:
        m.show_in_browser()
    print("Done.")
    return m

def getTableHtml(df, region, col):
    table = getGroupTable(df, "Region", col) # get unique counts of col
    t = table[table["Region"].values == region] # filter to just specified region
    t =t.drop(labels="Region",axis=1) # remove region column
    return t.to_html(index=False) # return as html w/ no indices

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<csvPath>")
        exit(1)
    os.makedirs(imagesDir, exist_ok = True)
    main(sys.argv[1])