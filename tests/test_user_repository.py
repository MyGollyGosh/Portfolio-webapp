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

'''
Given an id
#get_by_id returns the user with that id
'''
def test_get_by_id_returns_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.get_by_id(2) == User('janedoe', 'janedoe@example.com', 'Password!2', 2)

'''
Given an id that does not exist
#get_by_id returns message saying no user
'''
def test_no_valid_id_returns_message(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(IndexError) as e:
        repo.get_by_id(3)
    assert str(e.value) == 'No user with id 3 found'

'''
Given an existing username and password
#validate_user returns True
'''
def test_valid_user_is_validated(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.validate_user('johndoe', 'Password!1') == True

'''
Given an invalid username and valid password
#validate_user returns False
'''
def test_invalid_username_is_not_validated(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.validate_user('jimothydoe', 'Password!1') == False

'''
Given a valid username and invalid password
#validate_user returns False
'''
def test_invalid_password_is_not_validated(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.validate_user('johndoe', 'Password!') == False

'''
Given an ID
#delete_by_id will remove the user with that ID from the DB
'''
def test_delete_with_id_removes_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.delete_by_id(1) == 'User with id 1 successfully deleted'
    assert repo.all() == [
        User('janedoe', 'janedoe@example.com', 'Password!2', 2)
        ]
    
'''
Given an ID that doesn't exist
#delete_by_id returns an error message
'''
def test_invalid_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(IndexError) as e:
        repo.delete_by_id(3)
    assert str(e.value) == 'No user with id 3 found'

'''
Given a valid password and id
#update_user changes the password
'''
def test_valid_password_is_changed(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    repo.update_user('Password#2', 2)
    assert repo.get_by_id(2).password == 'Password#2'

'''
Given an invalid password and valid id
#update_user does not change password
and returns error message stating so
'''
def test_invalid_password_is_not_changed(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.update_user('Password2', 2)
    assert str(e.value) == 'Password could not be changed: Invalid password'

'''
Given a valid password and an invalid ID
#update_user returns an error
'''
def test_invalid_id_gives_error_on_update(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.update_user('Password#2', 20)
    assert str(e.value) == f'Password could not be changed: No user found'