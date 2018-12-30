import os
import pandas
import folium
from django.templatetags.static import static
from pathlib import Path

def generate_map():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    url_app = BASE_DIR + "/qaweb"
    url_file = url_app + str(static("qaweb/files/coordenadas.xlsx"))
    url_map = url_app + "/templates/qaweb/map.html"

    print("url_file: %s" % url_file)

    my_file = Path(url_file)

    if my_file.exists():
        df = pandas.read_excel(url_file)

        zona = list(df["Zona"])
        lat = list(df["Latitud"])
        lon = list(df["Longitud"])
        notas = list(df["Notas"])
        
        def color_producer(longitud):
            if longitud > -4.50:
                return 'green'
            elif -4.50 >= longitud > -5:
                return 'orange'
            else:
                return 'red'

        mapa = folium.Map(location=[36.84, -4.78], zoom_start=8, tiles="Mapbox Bright")

        fg = folium.FeatureGroup(name="QAClimb Map")

        for zn, lt, ln, nts in zip(zona, lat, lon, notas):
            #fg.add_child(folium.Marker(location=[lt, ln], popup=zn + "<br/>" + nts, icon=folium.Icon(color='blue')))
            fg.add_child(folium.CircleMarker(location=[lt, ln],
                                             radius = 6,
                                             popup=zn + "<br/>" + nts,
                                             fill_color=color_producer(ln),
                                             color = 'grey',
                                             fill = True,
                                             fill_opacity=0.8))

        mapa.add_child(fg)

        mapa.save(url_map)
    else:
        print("The file1 doesnt exist")
        print(url_file)
        print(my_file)