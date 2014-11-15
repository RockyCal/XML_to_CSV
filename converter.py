__author__ = 'Raquel'

import xml.etree.ElementTree as eTree
from urllib.request import urlopen
# Find:
#  - Name
#  - Description
#  - URL
#  - Type
#  - Organization

url = 'http://hydro10.sdsc.edu/metadata/NOAA_NGDC/35CE47CA-CD42-4897-9385-A34269DCC479.xml'

tree = eTree.parse(urlopen(url))
root = tree.getroot()

idInfo = root.find('{http://www.isotc211.org/2005/gmd}identificationInfo').find('{http://www.isotc211.org/2005/gmd}'
                                                                                'MD_DataIdentification')
citation = idInfo.find('{http://www.isotc211.org/2005/gmd}citation').find('{http://www.isotc211.org/2005/gmd}'
                                                                          'CI_Citation')
title = citation.find('{http://www.isotc211.org/2005/gmd}title').\
    find('{http://www.isotc211.org/2005/gco}CharacterString').text