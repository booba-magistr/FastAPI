# Метод для создания JWT access_token
# Метод для трансформации пароля в hash строку
# Метод для проверки соответствия пароля и hash-строки
# Метод который будет принимать Email (логин) и пароль от пользователя, чтобы выполнить аутинтефикацию.
####################### Для хэширования паролей #######################
from passlib.context import CryptContext
####################### Для генерации JWT токена ####################### 
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.config import get_auth_data


# Контекст для хэширования паролей
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# CryptContext настраивается для использования алгоритма bcrypt
# deprecated="auto" - использовать рекомендованные схемы хэширования и авт. обновлять устаревшие

def get_password_hash(password:str):
    return password_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return password_context.verify(plain_password, hashed_password)
