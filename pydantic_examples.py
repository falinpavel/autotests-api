from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str

class UserFullData(User):
    email: str
    phone_number: str
    course_id: int
    is_active: bool = True # Значение по умолчанию

class SpecificUserData(BaseModel):
    specific_data: str = Field(alias="specificData")

class Address(BaseModel):
    street: str
    city: str
    state: str

class StructureWithAddress(UserFullData):
    address: Address

response_specific = {
    "specificData": "specific-value"
}
specific = SpecificUserData(**response_specific)
print(specific)

user = UserFullData(
    id=1,
    name="name-user",
    email="email-full-data",
    phone_number="phone_number-full-data",
    course_id=123,
    is_active=True
)

print(user)
print(user.model_dump())
print(user.model_dump_json())

structure_with_address = StructureWithAddress(
    id=123,
    name="name-user",
    email="email-full-data",
    phone_number="phone_number-full-data",
    course_id=123,
    is_active=False,
    address=Address(
        street="street-full-data",
        city="city-full-data",
        state="state-full-data"
    )
)
print(structure_with_address)
print(structure_with_address.model_dump())
print(structure_with_address.model_dump_json())