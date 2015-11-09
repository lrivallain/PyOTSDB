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
        try:
            print(self.endpoint)
            # request & fetch response
            response = requests.post(self.endpoint,
                                     data=json.dumps(data),
                                     auth=(self.username, self.password))

            # raise error ?
            response.raise_for_status()

            # return the body of response
            return response.content

        except requests.exceptions.HTTPError as e:
            # in case of error print HTTP code and return nothing
            print('HTTP code is %d' % e.response.status_code)
            return "[]"


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
    def _http_get(self, start, queries):
        data = {
            'start': start,
            'queries' : queries
        }
        print(json.dumps(data))
        return self._http_request(data)


    # push data through telnet
    def _telnet_put(self, metric_name, timestamp, value, tags):
        pass # not yet available


    # get data through telnet
    def _telnet_get(self, start, end, queries):
        pass #not yet available


    # push data
    def put(self, metric_name, timestamp=int(time.time()), value=0, tags={}):
        if self.endpoint.startswith("http"):
            return self._http_put(metric_name, timestamp, value, tags)
        else:
            return self._telnet_put(metric_name, timestamp, value, tags)


    # get data
    def get(self, start, queries=[]):
        if self.endpoint.startswith("http"):
            return self._http_get(start, queries)
        else:
            return self._telnet_get(start, queries)
