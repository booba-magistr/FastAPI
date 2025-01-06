from fastapi import APIRouter, HTTPException, status
from .auth import get_password_hash
from .dao import UsersDAO
from .schemas import SchemaUserRegistration


user_router = APIRouter(prefix='/users', tags=['Пользователи'])

@user_router.post('/register/', summary='Register users')
async def register_user(user_data: SchemaUserRegistration):
    user = await UsersDAO.get_user_by_email(email=user_data.email)
    
    if user:
        raise HTTPException(
                            status_code=status.HTTP_409_CONFLICT,
                            detail='Данный пользователь уже зарегистрирован'
                            )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return {'status': 'success', 'message': 'Вы успешно зарегистрировались'}