from http import HTTPStatus
import allure
import pytest

from data import get_pet_endpoints
from data.data import PetData
from generator.pet_generator import PetGenerator
from src.assertions import Assertions
from src.http_methods import MyRequests
from src.prepare_data.prepare_pet_data import PreparePetData, PrepareDynamicPetData
from src.schemas import CreatePetSchemas
from src.validator import Validator


@allure.epic('Testing create pet')
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()
    pet_data = PreparePetData()
    dynamic_pet_data = PrepareDynamicPetData()
    pet_generator = PetGenerator()

    # Если создавать json-файл отдельно и передавать его в post-запросе
    def test_create_pet_1(self, get_test_name):
        data = self.pet_data.get_pet_json()
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(response=response, expected_status_code=HTTPStatus.OK,
                                           test_name=get_test_name)
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)
        print(response.text)

    # Если нужно генерировать данные json:
    def test_create_pet_2(self, get_test_name):
        info = next(self.pet_generator.generate_pet())  # можно передавать значения ключей, например, id = "Hello"
        data = self.dynamic_pet_data.prepare_pet_json(
            info)  # можно добавить параметр key = "name" и удалить этот ключ из data (id генерируется автоматически)
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(response=response, expected_status_code=HTTPStatus.OK,
                                           test_name=get_test_name)
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)

    @allure.title('Create pet')
    @pytest.mark.parametrize("status", PetData.status)
    def test_create_pet_3(self, get_test_name, status):
        info = next(self.pet_generator.generate_pet(status=status))
        data = self.dynamic_pet_data.prepare_pet_json_2(info)
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(response=response, expected_status_code=HTTPStatus.OK,
                                           test_name=get_test_name)
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)