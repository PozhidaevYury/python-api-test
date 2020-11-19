import configparser
import json
import os
import sys
import requests

from src.logging import Logger
from src.response import AssertableResponse

step = 0


def step_count():
    global step
    step = step + 1
    return step.__str__()


def read_ini():
    config_file_name = os.environ.get("config-file", "project.config.ini")
    root_path = os.path.join(sys.path[0], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


class ApiService(object):

    def __init__(self):
        self.base_url = os.environ.get("config-file", "project.config.ini")
        self.headers = {"content-type": "application/json"}

    def _post(self, url, body, headers=""):
        # self.headers["token"] = headers
        return requests \
            .post(url=read_ini()["DEFAULT"]["base_url"] + url,
                  data=json.dumps(body),
                  headers=self.headers
                  )

    def auth(self):
        return requests \
            .post(url=read_ini()["DEFAULT"]["base_url"]) \
            .json()["token"]


class UserApiService(ApiService):
    logger = Logger("test_user_registration.log").get_logger()

    def __init__(self):
        super().__init__()

    def create_user(self, user):
        # token = self.auth()
        response = self._post("/register", user)

        self.logger.info(
            step_count() + ")" "Request url={} body={}".format(response.request.url, response.request.body))
        self.logger.info(
            step_count() + ")" + "Response status={} body={}".format(response.status_code, response.text))

        return AssertableResponse(response, self.logger)
