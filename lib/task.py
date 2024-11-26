from datetime import datetime, date

class Task:
    def __init__(self, user_id, description, due_date, date_added, priority, status, id=None) -> None:
        self.id = id
        self.user_id = user_id
        check_valid_user_id(user_id)
        self.description = description
        check_valid_description(description)
        self.due_date = due_date
        check_valid_due_date(due_date)
        self.date_added = date_added
        check_valid_date_added(date_added)
        self.priority = priority
        check_valid_priority(priority)
        self.status = status
        check_valid_status(status)

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Task({self.user_id}, {self.description}, {self.due_date}, {self.date_added}, {self.priority}, {self.status}, {self.id})"



def check_valid_user_id(user_id) -> None:
    if type(user_id) != int:
        raise TypeError('Ensure valid user id (int)')

    
def check_valid_description(description) -> None:
    if type(description) != str:
        raise TypeError('Description must be a string')
    if len(description) < 3:
        raise ValueError('Invalid description')

    
def check_valid_due_date(due_date) -> None:
    if not isinstance(due_date, date):
        raise TypeError('Ensure valid due_date (date(YYYY, MM, DD))')

    
def check_valid_date_added(date_added) -> None:
    if not isinstance(date_added, datetime):
        raise TypeError('Ensure valid date_added (datetime(YYYY,MM,DD, HH,MI,SS))')


def check_valid_priority(priority) -> None:
    if type(priority) != int:
        raise TypeError('Ensure valid priority (int 1-5)')


def check_valid_status(status) -> None:
    if type(status) != str:
        raise TypeError('Ensure valid status (str)')
    
