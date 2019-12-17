'''
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
from craigslist import CraigslistJobs
cl_e = CraigslistJobs(site='newyork', category='fbh', 
						filters={'search_distance': 5, 'zip_code': 11423})
for result in cl_e.get_results(sort_by='newest', geotagged='true', limit=	500):
	#filter out non-dishwashers
	#thisOne = json.loads(result)
	if "dishwasher" or "dish" in result['name']:
		print(result['name']+'\n')
		print('url: ' + result['url'] + '\n')
		print('where: ')
		print(result['where'])
		print('\n')
