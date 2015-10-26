# -*- coding: utf8 -*-

import os
import time
import sys


# check inputs
if len(sys.argv) < 2:
    exit('Missing args  %s temp.indoor temp.outdoor' % sys.argv[0])


# check configuration
token_id = os.environ.get('PYOTSBD_OPENSTDB_USERNAME')
if not token_id:
    exit("Please : export PYOTSBD_OPENSTDB_USERNAME='XXXXXXXXX'")

token_key = os.environ.get('PYOTSBD_OPENSTDB_PASSWORD')
if not token_key:
    exit("Please : export PYOTSBD_OPENSTDB_PASSWORD='XXXXXXXXX'")

end_point = os.environ.get('PYOTSBD_ENDPOINT')
if not end_point:
    exit("Please : export PYOTSBD_ENDPOINT='https://opentsdb.iot.runabove.io'")
end_point = u"%s/api/put" % end_point

source = os.environ.get('PYOTSBD_HOSTNAME')
if not source:
    exit("Please : export PYOTSBD_HOSTNAME=$(hostname -s)")



# Raw body data to send
data = [
    {
        'metric': 'home.temp.indoor',
        'timestamp': int(time.time()),
        'value': float(sys.argv[1]),
        'tags': {
            'source': source
        }
    },
    {
        'metric': 'home.temp.outdoor',
        'timestamp': int(time.time()),
        'value': float(sys.argv[2]),
        'tags': {
            'source': source
        }
    },
]


from PyOTSDB import PyOTSDB
con = PyOTSDB(endpoint=end_point, username=token_id, password=token_key)
con.put(data)

