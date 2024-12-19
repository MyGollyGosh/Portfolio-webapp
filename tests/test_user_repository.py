from lib.user import User
from lib.user_repository import UserRepository
import pytest
from werkzeug.security import generate_password_hash, check_password_hash

'''
When I call #all
I get a list of every user
Note: The passwords in the response will be hashed
'''
def test_all_returns_every_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    users = repo.all()
    assert len(users) == 2
    assert users[0].username == 'johndoe'
    assert users[0].email == 'johndoe@example.com'
    assert users[0].id == 1
    assert check_password_hash(users[0].password, 'Password!1')
    assert users[1].username == 'janedoe'
    assert users[1].email == 'janedoe@example.com'
    assert users[1].id == 2
    assert check_password_hash(users[1].password, 'Password!2')

'''
Given a username, email and password as a User object
#add puts an extra user in the DB and hashes the password
'''
def test_add_with_correct_details_adds_new_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    repo.add('jimdoe', 'jimdoe@example.com', 'Password!3')
    users = repo.all()
    assert len(users) == 3
    new_user = users[2]
    assert new_user.username == 'jimdoe'
    assert new_user.email == 'jimdoe@example.com'
    assert new_user.id == 3
    assert check_password_hash(new_user.password, 'Password!3')

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
    assert len(repo.all()) == 2

def test_empty_username_returns_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add(' ', 'jimdoe@example.com', 'Password!3')
    assert str(e.value) == 'Username cannot be empty'
    assert len(repo.all()) == 2

'''
Given an invalid email
#add returns an error and nothing is added to the DB
'''
def test_invalid_email_returns_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add('jimdoe', 'jimdoeexample.com', 'Password!3')
    assert str(e.value) == 'Invalid email'
    assert len(repo.all()) == 2

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
    assert len(repo.all()) == 2

'''
Given an id
#get_by_id returns the user with that id
'''
def test_get_by_id_returns_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    user = repo.get_by_id(2)
    assert user.username == 'janedoe'
    assert user.email == 'janedoe@example.com'
    assert user.id == 2
    assert check_password_hash(user.password, 'Password!2')

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
#validate_user returns True and the user object
'''
def test_valid_user_is_validated(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    is_valid, user = repo.validate_user('johndoe', 'Password!1')
    assert is_valid == True
    assert user.username == 'johndoe'
    assert user.email == 'johndoe@example.com'
    assert user.id == 1

'''
Given an invalid username and valid password
#validate_user returns False and None
'''
def test_invalid_username_is_not_validated(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    is_valid, user = repo.validate_user('jimothydoe', 'Password!1')
    assert is_valid == False
    assert user is None

'''
Given a valid username and invalid password
#validate_user returns False and None
'''
def test_invalid_password_is_not_validated(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    is_valid, user = repo.validate_user('johndoe', 'Password!')
    assert is_valid == False
    assert user is None

'''
Given an ID
#delete_by_id will remove the user with that ID from the DB
'''
def test_delete_with_id_removes_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.delete_by_id(1) == 'User with id 1 successfully deleted'
    users = repo.all()
    assert len(users) == 1
    assert users[0].username == 'janedoe'

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
#update_user changes the password and hashes it
'''
def test_valid_password_is_changed(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    repo.update_user('Password#2', 2)
    updated_user = repo.get_by_id(2)
    assert check_password_hash(updated_user.password, 'Password#2')
    # assert check_password_hash(new_user.password, 'Password!3')
    

'''
Given an invalid password and valid id
#update_user does not change password
and returns error stating so
'''
def test_invalid_password_is_not_changed(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.update_user('Password2', 2)
    assert str(e.value) == 'Password could not be changed: Invalid password'

'''
Given a valid password and an invalid ID
#update_user does not change password
and returns error stating so
'''
def test_invalid_id_gives_error_on_update(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.update_user('Password#2', 20)
    assert str(e.value) == 'Password could not be changed: No user found'

'''
Test get_by_username 
returns correct user
'''
def test_get_by_username_returns_correct_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    user = repo.get_by_username('johndoe')
    assert user.username == 'johndoe'
    assert user.email == 'johndoe@example.com'
    assert user.id == 1
    assert check_password_hash(user.password, 'Password!1')

'''
Test get_by_username 
returns None for non-existent user
'''
def test_get_by_username_returns_none_for_invalid_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    assert repo.get_by_username('nonexistent') is None