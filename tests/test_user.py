from lib.user import User


'''
Given a username, email and password
a User class is initialisted
'''

def test_init():
    user = User('username', 'email@example.com', 'password')
    assert user.id == None
    assert user.username == 'username'
    assert user.email == 'email@example.com'
    assert user.password == 'password'
    