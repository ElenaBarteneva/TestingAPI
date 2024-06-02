import json

import allure


class BaseTestData:

    def format_data_as_json(self, data):
        return json.dumps(data)

    @staticmethod
    def attach_request(request):
        req = json.dumps(request, indent=4)
        allure.attach(name='Request', body=req, attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_response(response):
        resp = json.dumps(response, indent=4)
        allure.attach(name='Response', body=resp, attachment_type=allure.attachment_type.JSON)
