import abc
from hamcrest import assert_that
import jsonpath_rw


class Conditions(object):

    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response, logger):
        return


class StatusCodeConditions(Conditions):

    def __init__(self, code):
        super().__init__()
        self.status_code = code

    def __repr__(self):
        return "status code is {}".format(self.status_code)

    def match(self, response, logger):
        if response.status_code == self.status_code:
            logger.info("Assert: status code should be {}".format(self.status_code))
        else:
            logger.error("Assert: status code should be {}".format(self.status_code))

        assert response.status_code == self.status_code


status_code = StatusCodeConditions


class BodyFieldConditions(Conditions):

    def __init__(self, json_path, matcher):
        super().__init__()
        self.json_path = json_path
        self.matcher = matcher

    def __repr__(self):
        return "body field {} {}".format(self.json_path, self.matcher)

    def match(self, response, logger):
        if len(self.json_path) > 0:
            logger.info("Assert: json value has {}".format(self.matcher))
        else:
            logger.error("Assert: json value has {}".format(self.matcher))

        json_value = jsonpath_rw.parse(self.json_path).find(response.json())
        assert_that(json_value, self.matcher)


body = BodyFieldConditions
