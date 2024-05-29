from functions import get_json_data


class PreparePetData:

    def get_pet_json(self):
        json_data = get_json_data("pet_data.json")
        return json_data
