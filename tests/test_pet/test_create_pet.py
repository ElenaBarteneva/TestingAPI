from http import HTTPStatus
import allure
from data import get_pet_endpoints
from src.assertions import Assertions
from src.http_methods import MyRequests
from src.schemas.create_pet_schema import CreatePetSchema
from src.validator import Validator


@allure.epic('Testing create pet')
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()

    def test_create_pet(self, get_test_name):
        data = """{
          "id": 12999,
          "category": {
            "id": 0,
            "name": "string7777"
          },
          "name": "doggie",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 555555,
              "name": "string"
            }
          ],
          "status": "available"
        }"""
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(response=response, expected_status_code=HTTPStatus.CREATED, test_name=get_test_name)
        self.validator.validate_response(response=response, model=CreatePetSchema.create_pet)
        print(response.text)
