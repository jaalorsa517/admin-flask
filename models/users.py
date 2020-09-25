from flask_login import UserMixin


class user(UserMixin):
    def __init__(self, nickname, password):
        self.id = None
        self.nickname = nickname
        self.password = password
        self.role = None
