

class User:
    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password