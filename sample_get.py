# -*- coding: utf8 -*-

import os
import time
import sys
import random


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
end_point = u"%s/api/put" % end_point

source = os.environ.get('PYOTSDB_HOSTNAME')
if not source:
    exit("Please : export PYOTSDB_HOSTNAME=$(hostname -s)")

delta = os.environ.get('PYOTSDB_DELTA')
if not delta:
    exit("Please : export PYOTSDB_DELTA=XX")
delta = int(delta)*60*60



from PyOTSDB import PyOTSDB
con = PyOTSDB(endpoint=end_point, username=token_id, password=token_key)


startpoint = int(time.time())-delta


print("Getting the count of points since 24h for indoor t°")
res = con.get(start=startpoint,
              queries = [{
                  "metric": "home.temp.indoor",
                  "aggregator": "sum",
                  #"tags": {
                  #    "source": source
                  #}
              }]
      )

print(res)
