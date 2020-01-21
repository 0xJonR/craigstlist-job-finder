import json
import datetime
from craigslist import CraigslistForSale
import sys

cl_e = CraigslistForSale(site='newyork', filters={'search_distance':5, 'zip_code':11423, 'has_image':True, 'max_price':5000, 'min_price':1000}, category='cta')

#search terms
vars = set() #input vars
if len(sys.argv) >= 2:
    for x in range(1, len(sys.argv)):
        vars.add(str.upper(sys.argv[x]))
else:
    vars = {'HONDA', 'CIVIC', 'ACURA', 'TSX', 'MAZDA3'} #default search


print(datetime.datetime.now())
for result in cl_e.get_results(sort_by='newest', limit=666):
    for subst in vars:
        if subst in str.upper(result['name']):
            print(result['name'])
            print(result['price'])
            print(result['url'])
            print(result['datetime'])
            print()
