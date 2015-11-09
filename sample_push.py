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

period = int(os.environ.get('PYOTSDB_PERIOD'))
if not period:
    exit("Please : export PYOTSDB_PERIOD=YY")


# init pyotsb worker
from PyOTSDB import PyOTSDB
con = PyOTSDB(endpoint=end_point, username=token_id, password=token_key)

while True:
    timer = int(time.time())
    print("sending indoor t°")
    con.put(metric_name='home.temp.indoor',
            timestamp=timer,
            value=random.randrange(20, 25),
            tags = {
                'source': source,
            })

    print("sending outdoor t°")
    con.put(metric_name='home.temp.outdoor',
            timestamp=timer,
            value=random.randrange(10, 16),
            tags = {
                'source': source,
            })
    print("waiting %d seconds..." % period)
    time.sleep(period)
