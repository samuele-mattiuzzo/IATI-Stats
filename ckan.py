import os,json
from collections import defaultdict

out = defaultdict(dict)

# The ckan directory is the one produced by https://github.com/Bjwebb/IATI-Registry-Refresher/tree/save_ckan_json

for publisher in os.listdir('ckan'):
    with open(os.path.join('ckan', publisher)) as fp:
        for package in json.load(fp)['result']:
            if package['resources']:
                extras = dict((x['key'], x['value']) for x in package['extras'])
                out[publisher][package['name']] = {
                    'title': package['title'],
                    'extras': extras,
                    'license_id': package['license_id'],
                    'resource': package['resources'][0],
                }

with open('ckan.json', 'w') as fp:
    json.dump(out, fp,  indent=2, sort_keys=True)
