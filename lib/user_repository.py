from lib.user import User

class UserRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self) -> list:
        rows = self._connection.execute('SELECT * FROM users;')
        return [User(row['username'], row['email'], row['password_hash'], row['id']) for row in rows]
    
    def get_by_id(self, id) -> object:
        try:
            user = self._connection.execute('SELECT * FROM users WHERE id = %s', (id,))[0]
        except:
            raise IndexError(f'No user with id {id} found')
        else:
            return User(user['username'], user['email'], user['password_hash'], user['id'])
        
    def validate_user(self, username, password) -> bool:
        try:
            self._connection.execute('SELECT * FROM users WHERE username = %s AND password_hash = %s', (username, password))[0]
        except:
            return False
        else:
            return True
        
    def add(self, username, email, password) -> str:
        user = User(username, email, password)
        self._connection.execute('INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)', [username, email, password])
        return f"{user} was successfully created"
    
    def delete_by_id(self, id) -> str:
        user = self.get_by_id(id)
        if user != IndexError:
            self._connection.execute('DELETE FROM users WHERE id = %s', (id,))
            return f'User with id {id} successfully deleted'
        else:
            return f'No user with id {id} found'
        
    def update_user(self, password, id) -> str:
        try:
            user = self.get_by_id(id)
            user.check_valid_password(password)
            self._connection.execute('UPDATE users SET password_hash = %s WHERE id = %s', [password, id])
            return f'User with id {id} successfully changed password'
        except IndexError:
            raise ValueError('Password could not be changed: No user found')
        except ValueError as e:
            raise ValueError(f'Password could not be changed: {str(e)}')