from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users;')
        return [User(row['username'], row['email'], row['password_hash'], row['id']) for row in rows]
    
    def add(self, username, email, password) -> str:
        user = User(username, email, password)
        self._connection.execute('INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)', [username, email, password])
        return f"{user} was successfully created"