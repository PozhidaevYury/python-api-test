import configparser
import json
import os
import sys
import requests
import allure

from src.logging import Logger
from src.response import AssertableResponse


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
    logger = Logger() \
        .create_log_file("test_user_registration.log") \
        .get_logger()

    def __init__(self):
        super().__init__()

    @allure.step
    def create_user(self, user):
        # token = self.auth()
        return AssertableResponse(self._post("/register", user), self.logger)
