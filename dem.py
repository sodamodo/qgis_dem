from osgeo import ogr
import os

driver = ogr.GetDriverByName("ESRI Shapefile")


box_shapefile = "./NED_Reference/ned_13arcsec_g.shp"
california_shapefile = "./CA_state_reproject.shp"

box_datasource = driver.Open(box_shapefile, 0)
box_layer = box_datasource.GetLayer()

california_datasource = driver.Open(california_shapefile, 0)
california_layer = box_datasource.GetLayer()


for box_feature in box_layer:
    box_geom = box_feature.GetGeometryRef()
    for california_feature in california_layer:
        california_geom = box_feature.GetGeometryRef()
        if (box_geom.Intersects(california_geom)):
            print(box_feature.GetField("FILE_ID"))
