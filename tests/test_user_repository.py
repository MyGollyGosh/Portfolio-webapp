from lib.user import User
from lib.user_repository import UserRepository


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