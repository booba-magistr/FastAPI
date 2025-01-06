from pydantic import BaseModel, EmailStr, Field, validator
import re


class SchemaUserRegistration(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=32, description='Имя')
    last_name: str = Field(..., min_length=3, max_length=32, description='Фамилия')
    phone_number: str = Field(..., description='Номер телефона с +')
    email: EmailStr = Field(..., description='E-mail')
    password: str = Field(..., min_length=5, max_length=30, description='Пароль')

    @validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{5,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 5 до 15 цифр')
        return value
    
class SchemaUserAuth(BaseModel):
    email: EmailStr = Field(..., description='Email')
    password: str = Field(..., min_length=5, max_length=30, description='Пароль от 5 до 30 символов')
