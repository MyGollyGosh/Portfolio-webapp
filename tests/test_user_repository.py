from lib.user import User
from lib.user_repository import UserRepository
import pytest


'''
When I call #all
I get a list of every user
'''
def test_all_returns_every_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.all() == [
        User('johndoe', 'johndoe@example.com', 'Password!1', 1),
        User('janedoe', 'janedoe@example.com', 'Password!2', 2)
        ]

'''
Given a username, email and password as a User object
#add puts an extra user in the DB
'''
def test_add_with_correct_details_adds_new_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    repo.add('jimdoe', 'jimdoe@example.com', 'Password!3')
    assert repo.all() == [
        User('johndoe', 'johndoe@example.com', 'Password!1', 1),
        User('janedoe', 'janedoe@example.com', 'Password!2', 2),
        User('jimdoe', 'jimdoe@example.com', 'Password!3', 3)
        ]

'''
Given an invalid username
#add returns an error and nothing is added to the DB
'''
def test_invalid_username_returns_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add('', 'jimdoe@example.com', 'Password!3')
    assert str(e.value) == 'Username cannot be empty'
    assert repo.all() == [
        User('johndoe', 'johndoe@example.com', 'Password!1', 1),
        User('janedoe', 'janedoe@example.com', 'Password!2', 2)
        ]


'''
Given an invalid email
#add returns an error and nothing is added to the DB
'''
def test_invalid_password_returns_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add('jimdoe', 'jimdoeexample.com', 'Password!3')
    assert str(e.value) == 'Invalid email'
    assert repo.all() == [
        User('johndoe', 'johndoe@example.com', 'Password!1', 1),
        User('janedoe', 'janedoe@example.com', 'Password!2', 2)
        ]

'''
Given an invalid password
#add returns an error and nothing is added to the DB
'''
def test_invalid_password_returns_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add('jimdoe', 'jimdoe@example.com', 'Password3')
    assert str(e.value) == 'Invalid password'
    assert repo.all() == [
        User('johndoe', 'johndoe@example.com', 'Password!1', 1),
        User('janedoe', 'janedoe@example.com', 'Password!2', 2)
        ]


