from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users;')
        return [User(row['username'], row['email'], row['password_hash'], row['id']) for row in rows]