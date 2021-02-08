'''
dataquest.io/blog/last-fm-api-python
'''

from  data.Last_fm_keys import *
import requests, json

import time
from IPython.core.display import clear_output

import requests_cache
requests_cache.install_cache()

'''
Need to provide a user-agent header to identify ourselfves
when making a request
'''

'''Function for doing requests'''
def lastfm_get(payload):

    # define headers and URL
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = API_key
    payload['format'] = 'json'

    response = requests.get(url, headers=headers,params=payload)

    return response

def json_print(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)

    print(text)

'''
r = lastfm_get({
    'method': 'chart.gettopartists'
})
'''
#json_print(r.json()['artists']['@attr'])


'''
Pagination
1. limit: The number of results to fetch per page
2. page: which page of the results we want to fetch

Rate limiting
1. Use: time.sleep()
2. Use a local database to cache the results
'''

# initialize list for results
responses = []

# set initial page and a high total number
page = 1
total_pages = 99999 # Dummy number to make the look start

while page <= total_pages:

    payload = {
        'method': 'chart.gettopartists',
        'limit': 500,
        'page': 1
    }

    # print some output so we can see the status
    print('Requesting page {}/{}'.format(page, total_pages))

    # clear the output to make things neater
    clear_output(wait = True)

    # make the API call
    response = lastfm_get(payload)

    # If we get an error, print the response and halt the loop
    if response.status_code !=200:
        print(response.text)
        break

    # extract Pagination info
    page = int(response.json()['artists']['@attr']['page'])
    total_pages = 2
    #total_pages = int(response.json()['artists']['@attr']['totalPages'])

    # append responses
    responses.append(response)

    # if it's not a cached result, sleep
    # At first check if it is not a cached result, return False
    if not getattr(response, 'from_cache', False):
        time.sleep(0.25)

    # increment the page number
    page += 1

import pandas as pd

r0 = responses[0]
r0_json = r0.json()

json_print(r0_json)
