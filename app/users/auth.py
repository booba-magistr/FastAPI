# Метод для создания JWT access_token
# Метод для трансформации пароля в hash строку
# Метод для проверки соответствия пароля и hash-строки
# Метод который будет принимать Email (логин) и пароль от пользователя, чтобы выполнить аутинтефикацию.
####################### Для хэширования паролей #######################
from passlib.context import CryptContext
####################### Для генерации JWT токена ####################### 
from jose import jwt
from datetime import datetime, timedelta, timezone
from config import get_auth_data
###############################################################
from pydantic import EmailStr
from .dao import UsersDAO


# Контекст для хэширования паролей
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# CryptContext настраивается для использования алгоритма bcrypt
# deprecated="auto" - использовать рекомендованные схемы хэширования и авт. обновлять устаревшие

def get_password_hash(password:str):
    return password_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    # plain_password - обычный пароль
    # hashed_password - хэшированный пароль
    return password_context.verify(plain_password, hashed_password)

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)  # 30 дней длится токен
    to_encode.update({'exp': expire})
    auth_data = get_auth_data()
    # кодировка данных в JWT с помощью секретного ключа и алгоритма шифрования
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt  # токен для аутентификации пользователей (далее он пойдёт в куки
    #  после чего его можно считывать)

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.get_user_by_email(email=email)
    if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
        return None
    return user
