import string
from typing import final

@final
class UserSignInRequest:
    def __init__(self, username: string, password: string):
        self._username = username
        self._password = password

    
