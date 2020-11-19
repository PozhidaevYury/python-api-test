from src.logging import Logger


class AssertableResponse(object):

    def __init__(self, response):
        self.response = response
        logger = Logger().get_logger()
        logger.info("Request \n url={} \n body={}".format(response.request.url, response.request.body))
        logger.info("Response \n status={} \n body={}".format(response.status_code, response.text))

    def status_code(self, code):
        return self.response.status_code == code

    def field(self, name):
        return self.response.json()[name]
