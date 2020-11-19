from src.logging import Logger


class AssertableResponse(object):

    logger = Logger().get_logger()

    def __init__(self, response):
        self.logger.info("Request url={} body={}".format(response.request.url, response.request.body))
        self.logger.info("Response status={} body={}".format(response.status_code, response.text))

        self.response = response

    def status_code(self, code):
        return self.response.status_code == code

    def field(self, name):
        return self.response.json()[name]
