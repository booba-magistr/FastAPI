from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, timezone
from config import get_auth_data
from .dao import UsersDAO
from .models import User


# Получаем значение токена(users_access_token) из кук
def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Данный токен отсутствует'
            )
    return token

async def get_current_user(token:str = Depends(get_token)):
    # Декодер для получения данных с которыми мы будем дальше работать (sub(user_id), exp(длительн. токена))
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=[auth_data['algorithm']])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Токен не валидный'
            )
    
    # Не истёк ли токен
    expire = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)  # переводим в питоновский формат
    if not expire or expire_time < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Токен истёк'
            )

    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Не найден ID пользователя'
            )
    
    user = await UsersDAO.get_one_or_nothing(int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found'
            )

    return user


async def get_current_admin_user(current_user:User = Depends(get_current_user)):
    if current_user.is_admin:
        return current_user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='У Вас нет прав доступа'
    )