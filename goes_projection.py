import os
import folium

m = folium.Map([15.5, -90], zoom_start=7)
merc = os.path.join("data", "20231631150-20231631940-GOES16-ABI-CAM-13-1000x1000.gif")


img = folium.raster_layers.ImageOverlay(
        name="GOES 16 BANDA 13",
        image=merc,
        bounds=[[6,-76], [24, -94.80]],
        opacity=0.6,
        interactive=True,
        cross_origin=False,
        zindex=1)
    

img.add_to(m)
folium.LayerControl().add_to(m)

m.save("index.html")