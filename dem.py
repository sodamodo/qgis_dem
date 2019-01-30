from osgeo import ogr
import os
import logging



driver = ogr.GetDriverByName("ESRI Shapefile")

box_shapefile = "./NED_Reference/ned_13arcsec_g.shp"
california_shapefile = "./CA_state_reproject.shp"

box_datasource = driver.Open(box_shapefile, 0)
box_layer = box_datasource.GetLayer()

california_datasource = driver.Open(california_shapefile, 0)
california_layer = california_datasource.GetLayer()

california_feature = california_layer.GetNextFeature()
california_geom = california_feature.GetGeometryRef()

selections = []
for box_feature in box_layer:
    box_geom = box_feature.GetGeometryRef()
    if (box_geom.Intersects(california_geom)):
        logging.warning(box_feature.GetField("FILE_ID"))
    # for california_feature in california_layer:
    #     california_geom = california_feature.GetGeometryRef()
    #     if (box_geom.Intersects(california_geom)):
    #         FILE_ID = box_feature.GetField("FILE_ID")
    #         if FILE_ID not in selections:
    #             selections.append(FILE_ID)
    #     logging.warning("====Below did not intersect=====")
    #     logging.warning(box_feature.GetField("FILE_ID"))



logging.warning(selections)
