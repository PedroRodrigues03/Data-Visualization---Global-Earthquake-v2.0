import json

from plotly.graph_objs import Layout
from plotly import offline

FILENAME = 'data/eq_30_days_m1_2023.json'

with open(FILENAME) as file:
    all_eq_data = json.load(file)

readable_file = 'data/readable_data.json'
with open(readable_file, 'w') as file:
    json.dump(all_eq_data, file, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_text,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}
    },
}]

map_title = all_eq_data['metadata']['title']
my_layout = Layout(title=map_title)
fig = {
    'data' : data,
    'layout' : my_layout
}

offline.plot(fig, filename='html/global_earthquakes_past_month.html')