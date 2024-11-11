from lib.user import User
import pytest


'''
Given a username, email and password
a User class is initialisted
'''
def test_init():
    user = User('username', 'email@example.com', 'Password!1')
    assert user.id == None
    assert user.username == 'username'
    assert user.email == 'email@example.com'
    assert user.password == 'Password!1'

'''
Given an empty username 
Returns error
'''
def test_empty_username_returns_error():
    with pytest.raises(ValueError) as e:
        User('', 'email@example.com', 'Password!1')
    assert str(e.value) == 'Username cannot be empty'

'''
Given an int as a username
Returns error
'''
def test_int_username_gives_error():
    with pytest.raises(TypeError) as e:
        User(123, 'email@example.com', 'Password!1')
    assert str(e.value) == 'Username must be string'

'''
Given an email without @ or a . 
Returns error
'''
def test_valid_email_no_at():
    with pytest.raises(ValueError) as e:
        User('username', 'emailexample.com', 'Password!1')
    assert str(e.value) == 'Invalid email'

def test_valid_email_no_dot():
    with pytest.raises(ValueError) as e:
        User('username', 'email@examplecom', 'Password!1')
    assert str(e.value) == 'Invalid email'

'''
Given an empty password
Returns error
'''
def test_empty_password_returns_error():
    with pytest.raises(ValueError) as e:
        User('username', 'email@example.com', '')
    assert str(e.value) == 'Invalid password'

'''
Given a password with no punctuation
Return an error
'''

def test_given_no_punnctuation_return_error():
    with pytest.raises(ValueError) as e:
        User('username', 'email@example.com', 'Password1')
    assert str(e.value) == 'Invalid password'

'''
Given password with no capital
Returns an error
'''
def test_no_capital_returns_error():
    with pytest.raises(ValueError) as e:
        User('username', 'email@example.com', 'password!1')
    assert str(e.value) == 'Invalid password' 

'''
Given password with no lowercase letter
Returns error
'''
def test_no_lowercase_returns_error():
    with pytest.raises(ValueError) as e:
        User('username', 'email@example.com', 'PASSWORD!1')
    assert str(e.value) == 'Invalid password'

'''
Given no number
Returns error
'''
def test_no_number_returns_error():
    with pytest.raises(ValueError) as e:
        User('username', 'email@example.com', 'Password!')
    assert str(e.value) == 'Invalid password'

'''
Test equality
'''
def test_equality():
    user1 = User('username', 'email@example.com', 'Password!1')
    user2 = User('username', 'email@example.com', 'Password!1')
    assert user1 == user2

'''
Test inequality
'''
def test_equality():
    user1 = User('username1', 'email@example.com', 'Password!1')
    user2 = User('username2', 'email@example.com', 'Password!1')
    assert user1 != user2

'''
Test formatting
'''
def test_formatting():
    user = User('username', 'email@example.com', 'Password!1')
    assert str(user) == f'User(None, username, email@example.com)'
