import requests
import json


class PyOTSDB:
    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint
        self.username = username,
        self.password = password

    def request(self, data):
        try:
            # request & fetch response
            response = requests.post(self.endpoint, data=json.dumps(data),
                                     auth=(self.username, self.password))

            # raise error ?
            response.raise_for_status()

            # print the http response code on success
            print('Send successful\nResponse code from server: {}'.
                  format(response.status_code))

        except requests.exceptions.HTTPError as e:
            print('HTTP code is {} and reason is {}'.format(e.response.status_code,
                                                            e.response.reason))
    

    def put(self, data):
        self.request(data)


    def get(self, data):
        pass
