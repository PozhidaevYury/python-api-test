class AssertableResponse(object):

    def __init__(self, response, logger):
        self.response = response
        self.logger = logger

    def status_code(self, code):
        if self.response.status_code == code:
            self.logger.info("Assert: status code should be {}".format(code))
        else:
            self.logger.error("Assert: status code should be {}".format(code))
        return self.response.status_code == code

    def field(self, name):
        return self.response.json()[name]
