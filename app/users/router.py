from fastapi import APIRouter, HTTPException, status, Response, Depends
from .auth import get_password_hash, authenticate_user, create_access_token
from .dao import UsersDAO
from .schemas import SchemaUserRegistration, SchemaUserAuth
from .dependencies import get_current_user, get_current_admin_user
from .models import User


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
    response.set_cookie(key='users_access_token', value=access_token, httponly=True)
    # httponly=True - куки должны быть доступны только через http или https (не доступны
    # скриптам JavaScript на стороне клиента) для повышения безопасности от атак XSS(межсайтовый скриптинг)
    return {'status': 'success', 'access_token': access_token, 'refresh_token': None}


@user_router.get('/profile/')
async def get_profile(user_data: User = Depends(get_current_user)):
    return user_data


@user_router.post('/logout/')
async def logout_user(response:Response):
    response.delete_cookie(key='users_access_token')
    return {'status': 'success', 'message': 'Вы вышли из системы'}


@user_router.get('/users_list/')
async def get_users_list(user_data: User = Depends(get_current_admin_user)):
    return await UsersDAO.get_all()


@user_router.get('/profile/')
async def get_profile(user_data: User = Depends(get_current_user)):
    return user_data