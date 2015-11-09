# -*- coding: utf8 -*-

import os
import time
import sys
import json


# check configuration
token_id = os.environ.get('PYOTSDB_OPENSTDB_USERNAME')
if not token_id:
    exit("Please : export PYOTSDB_OPENSTDB_USERNAME='XXXXXXXXX'")

token_key = os.environ.get('PYOTSDB_OPENSTDB_PASSWORD')
if not token_key:
    exit("Please : export PYOTSDB_OPENSTDB_PASSWORD='XXXXXXXXX'")

end_point = os.environ.get('PYOTSDB_ENDPOINT')
if not end_point:
    exit("Please : export PYOTSDB_ENDPOINT='https://opentsdb.iot.runabove.io'")
end_point = u"%s/api/query" % end_point

source = os.environ.get('PYOTSDB_HOSTNAME')
if not source:
    exit("Please : export PYOTSDB_HOSTNAME=$(hostname -s)")

delta = os.environ.get('PYOTSDB_DELTA')
if not delta:
    exit("Please : export PYOTSDB_DELTA=XX")
delta = int(delta)*60*60


# init pyotsb worker
from PyOTSDB import PyOTSDB
con = PyOTSDB(endpoint=end_point, username=token_id, password=token_key)

# making query
print("Getting the count of points since %sh for indoor t°" % os.environ.get('PYOTSDB_DELTA'))
res = con.get(start=int(time.time())-delta,
              queries = [{
                  "metric": "home.temp.indoor",
                  "aggregator": "count",
                  "tags": {
                      "source": os.uname()[1].split('.')[0]
                  }
              }]
      )
data = json.loads(res)

print res

# parsing results
print("%d items found in last %sh" % (len(data[0]['dps']), os.environ.get('PYOTSDB_DELTA')))

sum = 0
for x in data[0]['dps']:
    sum += data[0]['dps'][x]
print("Average t° during this period is: %.2f°C" % (1.0*sum/len(data[0]['dps'])))
