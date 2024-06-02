from src.schemas import create_pet_schema, pet_response_schema


class CreatePetSchemas:
    create_pet = create_pet_schema.CreatePetSchema
    create_pet2 = pet_response_schema.CreatePetSchema
