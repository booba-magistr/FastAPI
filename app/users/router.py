from fastapi import APIRouter, HTTPException, status, Response
from .auth import get_password_hash, authenticate_user, create_access_token
from .dao import UsersDAO
from .schemas import SchemaUserRegistration, SchemaUserAuth


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


@user_router.post('/login/', summary='Login user')
async def login_user(response: Response, user_data: SchemaUserAuth):
    user_auth = await authenticate_user(email=user_data.email, password=user_data.password)

    if user_auth is None:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неверная почта или пароль'
        )
    
    access_token = create_access_token({'sub': str(user_auth.id)})  # Создается JWT токен
    # Токен записывается в куку
    response.set_cookie(key='users_access_toke', value=access_token, httponly=True)
    # httponly=True - куки должны быть доступны только через http или https (не доступны
    # скриптам JavaScript на стороне клиента) для повышения безопасности от атак XSS(межсайтовый скриптинг)
    return {'access_token': access_token, 'refresh_token': None}