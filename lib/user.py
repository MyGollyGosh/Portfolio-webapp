import re
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, email, password, id=None) -> None:
        self.id = id
        self.username = username
        self.check_valid_username(username)
        self.email = email
        self.check_valid_email(email)
        self.password = password
        self.check_valid_password(password)

    def is_active(self):
        return True
        #This setup does not allow for deactivating accounts which is not an issue
        # with my current format so no validation logic currently needed

    def get_id(self):
        return str(self.id)

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"User({self.id}, {self.username}, {self.email})"
    
    def check_valid_username(self, username) -> None:
        if type(username) != str:
            raise TypeError('Username must be string')
        if len(username) < 1:
            raise ValueError('Username cannot be empty')
    
    def check_valid_email(self, email) -> None:
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email')
        
    def check_valid_password(self, password) -> None:
        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&:$]{6,200}$"
        pattern = re.compile(reg)
        match = re.search(pattern, password)
        if not match:
            raise ValueError('Invalid password')
