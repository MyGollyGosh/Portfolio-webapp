

class Task:
    def __init__(self, user_id, description, due_date, date_added, priority, status, id=None):
        self.id = id
        self.user_id = user_id
        self.check_valid_user_id(user_id)
        self.description = description
        self.check_valid_description(description)
        self.due_date = due_date
        self.check_valid_due_date(due_date)
        self.date_added = date_added
        self.check_valid_date_added(date_added)
        self.priority = priority
        self.check_valid_priority(priority)
        self.status = status
        self.check_valid_status(status)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Task({self.user_id}, {self.description}, {self.due_date}, {self.date_added}, {self.priority}, {self.status}, {self.id})"

    def check_valid_user_id(self, user_id) -> None:
        if type(user_id) != int:
            raise TypeError('Ensure valid user id (int)')

        
    def check_valid_description(self, description) -> None:
        if type(description) != str:
            raise TypeError('Description must be a string')
        if len(description) < 3:
            raise ValueError('Invalid description')

        
    def check_valid_due_date(self, due_date) -> None:
        if type(due_date) != str:
            raise TypeError('Ensure valid due_date (str YYYY-MM-DD)')

        
    def check_valid_date_added(self, date_added) -> None:
        if type(date_added) != str:
            raise TypeError('Ensure valid date_added (str YYYY-MM-DD HH-MI-SS)')


    def check_valid_priority(self, priority) -> None:
        if type(priority) != int:
            raise TypeError('Ensure valid priority (int 1-5)')


    def check_valid_status(self, status) -> None:
        if type(status) != str:
            raise TypeError('Ensure valid status (str)')
    
