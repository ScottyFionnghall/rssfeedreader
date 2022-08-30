# rss parser
# uses requests module to handle http requests and xml module to handle xml conversion

import requests
import xml.etree.ElementTree as ET
import re
def parse(rss):
    link = requests.get(rss) # send http request to rss link
    root = ET.fromstring(link.text) # convert xml to ElementTree
    description = root[0].find('description') # find tag with description name
    description = re.sub('[</p>]','',description.text) # remove [p] tags if they are there
    link = root[0].find('link') # find tag with link name
    title = root[0].find('title') # find tag with title name
    print(title.text,'\n',link.text,'\n',description,'\n') # print title, link and description