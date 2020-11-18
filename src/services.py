import json

import requests


class ApiService(object):

    def __init__(self):
        pass


class UserApiService(ApiService):

    def __init__(self):
        super().__init__()

    def create_user(self, user):
        return requests \
            .post(url="http://localhost:80/register",
                  data=json.dumps(user),
                  headers={"content-type": "application/json"}
                  )
