import datetime
import json
import sys
import urllib2

if __name__=='__main__':
    for dataId in sys.argv[1:]:
        url = 'https://nycopendata.socrata.com/views/%s' % (dataId)
        request = urllib2.urlopen(url)
        metadata = json.loads(request.read())
        print dataId, datetime.datetime.fromtimestamp(metadata['createdAt'])
