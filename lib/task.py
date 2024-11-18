from lib.user_repository import UserRepository

class Task:
    def __init__(self, user_id, description, due_date, date_added, priority, status, id=None):
        self.id = id
        self.user_id = user_id
        self.check_valid_user_id(user_id)
        self.description = description
        self.check_valid_description(description)
        self.due_date = due_date
        self.date_added = date_added
        self.priority = priority
        self.status = status

    def check_valid_description(self, description) -> None:
        if type(description) != str:
            raise TypeError('Description must be a string')
        if len(description) < 3:
            raise ValueError('Invalid description')
        
    def check_valid_user_id(self, user_id) -> None:
        if type(user_id) != int:
            raise TypeError('Ensure valid user id (int)')
        
        # below logic not working. Need to implement logic to check that user_id is in DB
        # try:
        #     user = UserRepository()
        #     user.get_by_id(user_id)
        # except IndexError:
        #     raise ValueError(f'No user with id {id} found')