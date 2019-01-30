# from PyQt4.QtCore import *
from qgis.core import *
import logging

input_path = "./CA_state_reproject.shp"

box_source =  QgsVectorLayer("./NED_Reference/ned_13arcsec_g.shp", "boxes", "ogr")
input_source =  QgsVectorLayer(input_path, "input", "ogr")

logging.warning("EOii")
logging.warning(box_source.name()) #gebaeude
logging.warning(input_source.name()) #ausschluss
logging.warning(input_source.featureCount())

selections=[] #declares it is a list
for f in box_source.getFeatures():
    for a in input_source.getFeatures():
        if a.geometry().intersects(f.geometry()):
            intersection = a.geometry().intersection(f.geometry())
            logging.warning("INTERSECTED")
            if f["FILE_ID"] not in selections:
                    selections.append( f["FILE_ID"] )
            #print intersection.exportToWkt()

            #same result with .within() and even with a and f switched (the docs aren't that clear on that)
            break #only one or less intersection are possible

logging.warning(selections)
# print(layers[0].selectedFeatureCount()) #It was selected
# print(layers[1].featureCount())

#
# logging.warning("WELL THE SCRIPT RUNS==========>")
#
# input_path = "./CA_state_reproject.shp"
#
# box_layer = QgsVectorLayer("./NED_Reference/ned_13arcsec_g.shp", "boxes", "ogr")
# input_layer =  QgsVectorLayer(input_path, "input", "ogr")
#
# logging.warning("Feature Count")

# selections=[] #i it is a list
# try:
#     for f in box_layer.getFeatures():
#         logging.warning("box featurez")
#         for a in input_layer.getFeatures():
#             logging.warning("cali feature")
#             if a.geometry().intersects(f.geometry()):
#                 warning.logging(a.geometry())
#                 intersection = a.geometry().intersection(f.geometry())
#                 #print intersection.exportToWkt()
#                 #same result with .within() and even with a and f switched (the docs aren't that clear on that)
#                 selections.append( f["FILE_ID"] )
#                 break #only one or less intersection are possible
# except:
#     logging.exception('')
#
# logging.warning("========FILE IDs============")
# logging.warning(selections)
# print(selections)
# print(layers[0].selectedFeatureCount()) #It was selected
# print(layers[1].featureCount())


#
# print(layers[0].name()) #gebaeude
# print(layers[1].name()) #ausschluss
#
