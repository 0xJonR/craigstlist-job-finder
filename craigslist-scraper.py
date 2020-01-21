'''
 <way id="12281519" version="4" timestamp="2014-05-05T12:07:36Z" changeset="22145464" uid="599436" user="zeromap">
from craigslist import CraigslistHousing
cl_h = CraigslistHousing(site='sfbay', area='sfc', category='roo',
                         filters={'max_price': 1200, 'private_room': True})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print(result)

{
    'id': u'4851150747',
    'name': u'Near SFSU, UCSF and NEWLY FURNISHED - CLEAN, CONVENIENT and CLEAN!',
    'url': u'http://sfbay.craigslist.org/sfc/roo/4851150747.html',
    'datetime': u'2015-01-27 23:44',
    'price': u'$1100',
    'where': u'inner sunset / UCSF',
    'has_image': False,
    'has_map': True,
    'geotag': (37.738473, -122.494721)
}
'''
import json
import datetime
from craigslist import CraigslistJobs
import sys 
cl_e = CraigslistJobs(site='newyork',  
						filters={'search_distance': 5, 'zip_code': 11423})
vars = set()
if len(sys.argv) >= 2:
    for x in range(1, len(sys.argv)):
        vars.add(str.upper(sys.argv[x]))
else:
    vars = {"DISHWASHER", "TUTOR", "DRIVER", "LIFEGUARD"} #default values 

print(datetime.datetime.now())
for result in cl_e.get_results(sort_by='newest', limit=2000):
    for subst in vars:
        if subst in str.upper(result['name']):
            print(result['name'])
            print(result['url'])
            print(result['datetime'])
            print('\n')
