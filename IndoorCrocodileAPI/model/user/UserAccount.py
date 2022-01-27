from typing import final

from model.user.User import User
from request_model import UserSignInRequest

@final
class UserAccount(object):
    def __init__(self):
        pass

    # Public
    def sing_in(user: UserSignInRequest):
        pass

    def sing_up(user: User):
        pass

    def sign_out():
        pass

    def change_password():
        pass

    def check_account_type():
        pass

    # Private
    def check_identity():
        pass

    

    