PyOTSDB
===================
PyOTSB is a very minimalist help to push and get data to an OpenTSDB backend.

For now it only supports HTTP through requests but it's planned to add a "telnet" support.

It also only accepts very simple queries but it may become more efficient in the future.

Push example
-------------
To push data, you need some information for your OpenTSDB backend:

 - a username/or token 
 - a password
 - a endpath/URI

You can try the sample file about pushing (random) data:

    export PYOTSDB_OPENSTDB_USERNAME="myusername"
    export PYOTSDB_OPENSTDB_PASSWORD="***************"
    export PYOTSDB_ENDPOINT="https://opentsdb.iot.runabove.io"
    export PYOTSDB_PERIOD=30
    export PYOTSDB_HOSTNAME=$(hostname -s)
    
    python sample_get.py

Basically it does:

    # basic modules
    import time
    import random
    
    # init pyotsb worker
    from PyOTSDB import PyOTSDB
    con = PyOTSDB(endpoint=end_point, username=token_id, password=token_key)
    
    con.put(metric_name='home.temp.indoor',
            timestamp=int(time.time()),
            value=random.randrange(20, 25),
            tags = {
                'source': "sourceName",
            })
Get example
-------------
As the push method, some informations are required to get values from the timeseries backend:
 - a username/or token 
 - a password
 - a endpath/URI

You can try the sample file about getting (random) data:

    export PYOTSDB_OPENSTDB_USERNAME="myusername"
    export PYOTSDB_OPENSTDB_PASSWORD="***************"
    export PYOTSDB_ENDPOINT="https://opentsdb.iot.runabove.io"
    export PYOTSDB_HOSTNAME=$(hostname -s) 
    export PYOTSDB_DELTA="24"
    
    python sample_get.py

Basically it does:

    # basic modules
    import time
    import json

    # init pyotsb worker
    from PyOTSDB import PyOTSDB
    con = PyOTSDB(endpoint=end_point, username=token_id, password=token_key)
    
    # making query
    res = con.get(start=int(time.time())-delta,
                  queries = [{
                      "metric": "home.temp.indoor",
                      "aggregator": "avg",
                      "tags": {
                          "source": sourceName
                      }
                  }]
          )
    data = json.loads(res)

