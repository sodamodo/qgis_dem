from osgeo import ogr
import os
import logging
import requests
import glob

# import wget
# import zipfile


def getBoxes(shapefile_path="./test_shape/test_shape.shp"):

    driver = ogr.GetDriverByName("ESRI Shapefile")

    box_shapefile = "./NED_Reference/ned_13arcsec_g.shp"
    input_shapefile = shapefile_path

    box_datasource = driver.Open(box_shapefile, 0)
    box_layer = box_datasource.GetLayer()
    input_datasource = driver.Open(input_shapefile, 0)
    input_layer = input_datasource.GetLayer()

    input_feature = input_layer.GetNextFeature()
    input_geom = input_feature.GetGeometryRef()

    selections = []
    for box_feature in box_layer:
        box_geom = box_feature.GetGeometryRef()
        if (box_geom.Intersects(input_geom)):
            selections.append(box_feature.GetField("FILE_ID"))

    return selections


def make_links(boxid_list):
    link_list = []
    for box_id in boxid_list:
        link = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/ArcGrid/USGS_NED_13_{}_ArcGrid.zip".format(box_id)
        link_list.append({"link": link, "box_id": box_id})
    return link_list

def download_files(link_list):
    chunk_size = 8096
    bytes_transferred = 0

    for link in link_list:
        logging.warning("Now downloading file {current_file} of {number_of_files}".format(current_file=link_list.index(link) + 1, number_of_files=len(link_list)))
        url = link["link"]
        # url = "https://commons.wikimedia.org/wiki/File:Random.jpg"
        r = requests.get(url, stream=True)
        with open('./data/{}.zip'.format(link["box_id"]), 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in r.iter_content(chunk_size):
                if chunk:
                    f.write(chunk)
                bytes_transferred += len(chunk)
                percentage = bytes_transferred/total_length * 100
                logging.warning("=====percentage=====")
                logging.warning(percentage)
        break

boxid_list = getBoxes()
logging.warning(boxid_list)
link_list = make_links(boxid_list)
logging.warning(link_list)
download_files(link_list)
logging.warning(os.listdir('./data'))



# r = requests.get(test_url["link"], stream=True)
# path = './data/{}'.format(test_url["box_id"])
# with open(path, 'wb') as f:
#     total_length = int(r.headers.get('content-length'))
#     for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
#         if chunk:
#             f.write(chunk)
#             f.flush()
