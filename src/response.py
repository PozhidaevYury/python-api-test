import allure

step = 0


def step_count():
    global step
    step = step + 1
    return step.__str__()


class AssertableResponse(object):

    def __init__(self, response, logger):
        self.logger = logger

        self.logger.info(
            step_count() + ")" "Request url={} body={}".format(response.request.url, response.request.body))
        self.logger.info(
            step_count() + ")" + "Response status={} body={}".format(response.status_code, response.text))
        self.response = response

    @allure.step('response should have {condition}')
    def should_have(self, condition):
        condition.match(self.response, self.logger)
        return self
