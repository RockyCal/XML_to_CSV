__author__ = 'Raquel'

import xml.etree.ElementTree as eTree
from urllib.request import urlopen
#import re

# Find:
#  - Name
#  - Description
#  - URL
#  - Type
#  - Organization
#  - Supporting Agency
#  - Synonyms/Other names
#  - keywords
#  - relatedTo: CINERGI

# tag for tying resources to CINERGI
cinergi = 'Category:Resource:CINERGI'
category = 'Category:'
gmd = '{http://www.isotc211.org/2005/gmd}MD_Metadata'
gmi = '{http://www.isotc211.org/2005/gmi}MI_Metadata'
url = 'http://hydro10.sdsc.edu/metadata/NOAA_NGDC/35CE47CA-CD42-4897-9385-A34269DCC479.xml'

tree = eTree.parse(urlopen(url))
root = tree.getroot()
if gmi not in root.tag and gmd not in root.tag:
    print("Not right format.")
    exit()

# find data ID info
md_id = root.find('{http://www.isotc211.org/2005/gmd}identificationInfo').find('{http://www.isotc211.org/2005/gmd}'
                                                                               'MD_DataIdentification')

citation = md_id.find('{http://www.isotc211.org/2005/gmd}citation').find('{http://www.isotc211.org/2005/gmd}'
                                                                         'CI_Citation')

# title
title = citation.find('{http://www.isotc211.org/2005/gmd}title').\
    find('{http://www.isotc211.org/2005/gco}CharacterString').text

# distribution info
distribution = root.find('{http://www.isotc211.org/2005/gmd}distributionInfo').find('{http://www.isotc211.org/'
                                                                                    '2005/gmd}MD_Distribution')
distributor = distribution.find('{http://www.isotc211.org/2005/gmd}distributor').find('{http://www.isotc211.org/'
                                                                                      '2005/gmd}MD_Distributor')
online = distributor.find('{http://www.isotc211.org/2005/gmd}distributorTransferOptions').\
    find('{http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions').find('{http://www.isotc211.org/2005/gmd}onLine')

# url (finally)
url = online.find('{http://www.isotc211.org/2005/gmd}CI_OnlineResource').\
    find('{http://www.isotc211.org/2005/gmd}linkage').find('{http://www.isotc211.org/2005/gmd}URL').text


# get resource type(s)
resourceTypes = []
types = root.findall('{http://www.isotc211.org/2005/gmd}hierarchyLevel')
for each in types:
    resourceTypes.append(each.text)

# responsible party bullshit
respParty = root.find('{http://www.isotc211.org/2005/gmd}contact').\
    find('{http://www.isotc211.org/2005/gmd}CI_ResponsibleParty')

# organization
organization = respParty.find('{http://www.isotc211.org/2005/gmd}organisationName').find('{http://www.isotc211.org/2005'
                                                                                         '/gco}CharacterString').text

# keywords
keywords = []
keyword_tags = md_id.findall('{http://www.isotc211.org/2005/gmd}descriptiveKeywords')
for each in keyword_tags:
    keyword_container = each.find('{http://www.isotc211.org/2005/gmd}MD_Keywords')
    someKeywords = keyword_container.findall('{http://www.isotc211.org/2005/gmd}keywords')
    for k in someKeywords:
        keyword_text = k.text
        keywords.append(k.text)
