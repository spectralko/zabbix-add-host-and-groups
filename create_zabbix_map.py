#############################################
#Created by r.ryabcev v.4.01.041022
#Add new functions: Create URLS on map
############################################

#Connect modules
from pyzabbix import ZabbixAPI
import json
import csv

#Init variables
zapi = ZabbixAPI('http://zabbix_url', user='Admin', password='zabbix')
map_file = csv.reader(open('map_file.csv'), delimiter=';')
link_file = csv.reader(open('links_file.csv'), delimiter=';')
url_file = csv.reader(open('urls_file.csv'), delimiter=';')
final_tpl = []
final_links = []
final_urls = []

#Create loops
for [station_id,station_name,zbx_station_id] in map_file:
        zabbix_map_tpl = {
                "selementid": station_id,
                "elements": [{"groupid": zbx_station_id}],
                "label": station_name,
                "elementtype": 3,
                "iconid_off": 2,
                "x": 400,
                "y": 400
                }
        final_tpl.append(zabbix_map_tpl)

for [link_id] in link_file:
        map_link = {
                "color": "00FF00",
                "selementid1": "434",
                "selementid2": link_id
                }
        final_links.append(map_link)

for [station_selement, station_name] in url_file:
        map_url = {
                "selementid": "436",
                "url": [{"sysmapelementurlid": "1", "selementid": "436", "name": "Жопа слона","url": "http://url/d/q09AvxVVz/zabbix-system-status?var-group=&orgId=1"}]
                }
        final_urls.append(map_url)

#Create functions
def map_cr():
        mapcreate = zapi.map.create(
        name = "Название карты",
        width = 600,
        height = 1000
        )
        print ("Map Created Succsesfully!")

def station_cr():
        map_update = zapi.map.update (
                sysmapid = 6,
                width = 600,
                height = 1000,
                selements = final_tpl,
        )
        print ("Elements created Succsesfully!")

def link_cr():
        link_update = zapi.map.update (
                sysmapid = 6,
                links = final_links
        )
        print ("Links created Succsesfully!")

def url_cr():
        url_update = zapi.map.update (
                sysmapid = 6,
                url = final_urls
        )
        print ("URLS created Succsesfully!")

def map_gt():
#Elements to output:
#        "output": "extend",
#        "selectSelements": "extend",
#        "selectLinks": "extend",
#        "selectUsers": "extend",
#        "selectUserGroups": "extend",
#        "selectShapes": "extend",
#        "selectLines": "extend",
#        "sysmapids": "3"

        map_get = zapi.map.get (
        selectUrls = "extend",
        sysmapids = 6
        )
        print (map_get)

#Call function
url_cr()
