import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
map= folium.Map(location=[38.2,-99.2],zoom_start=6, tiles= "Stamen Terrain")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000 :
        return 'orange'
    else:
        return 'red'

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

fgv= folium.FeatureGroup("Volcanoes")

for lt,lo,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,lo], radius=6, popup= str(el), fill_color= color_producer(el), color= 'grey', fill_capacity= 0.7))

fgp= folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r" ,encoding="utf-8-sig").read(), style_function= lambda x: {'fillColor': 'green'
if x['properties']['POP2005'] < 10000000  else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")