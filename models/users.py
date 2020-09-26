from flask_login import UserMixin
import csv


class User(UserMixin):
    path_csv = 'models/user.csv'
    fieldnames = ['name', 'password', 'role']

    def __init__(self, nickname='', password='', role=''):
        self.id = nickname
        self.password = password
        self.role = role

    @staticmethod
    def getUser(nickname):
        with open(User.path_csv) as csv_file:
            reader = csv.DictReader(csv_file, User.fieldnames)
            for user in reader:
                if nickname in user['name']:
                    return User(user['name'], user['password'], user['role'])
        return None

    @staticmethod
    def setUser(nickname, password, role=''):
        user = dict(name=nickname, password=password, role=role)
        with open(User.path_csv, 'a') as file:
            writer = csv.DictWriter(file, User.fieldnames)
            writer.writerow(user)
