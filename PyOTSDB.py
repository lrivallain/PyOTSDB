import requests
import json
import time


class PyOTSDB:
    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint
        self.username = username,
        self.password = password

    # general request through http
    def _http_request(self, data):
        #try:
            # request & fetch response
            #response = requests.post(self.endpoint, data=json.dumps(data),
            #                         auth=(self.username, self.password))

            response = requests.post("https://eeaaaiayr5ra5:ii2abAw1tRa8rTtZD8zrEF2r@opentsdb.iot.runabove.io/api/query", data=json.dumps(data))
            # raise error ?
            #response.raise_for_status()

            # print the http response code on success
            print('Send successful\nResponse code from server: {}'.
                  format(response.status_code))
            return response.content

        #except requests.exceptions.HTTPError as e:
        #    print('HTTP code is {} and reason is {}'.format(e.response.status_code,
        #                                                    e.response.reason))
    
    # push data through http
    def _http_put(self, metric_name, timestamp, value, tags):
        data = {
            'metric': metric_name,
            'timestamp': timestamp,
            'value': value,
            'tags': tags,
        }

        self._http_request(data)


    # get data through http
    def _http_get(self, start, end, queries):
        data = {
            'start': start,
            'queries' : queries
        }
        print(json.dumps(data))
        return self._http_request(data)


    # push data
    def put(self, metric_name, timestamp=int(time.time()), value=0, tags={}):
        if self.endpoint.startswith("http"):
            return self._http_put(metric_name, timestamp, value, tags)
        else:
            psss #not yet available


    # get data
    def get(self, start, end=None, queries=[]):
        if self.endpoint.startswith("http"):
            return self._http_get(start, end, queries)
        else:
            psss #not yet available
