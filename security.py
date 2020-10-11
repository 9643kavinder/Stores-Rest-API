from models.users import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    user  = UserModel.get_user_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.get_user_by_id(user_id)