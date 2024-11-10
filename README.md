# Task Manager

Feel free to follow along while I create this webapp and eventually host it serverless on AWS.

## Project Management

Track the development progress on my [Trello Board](https://trello.com/invite/b/6730abdb24a18a4847cfea14/ATTI6cbb8e35dafcfca1a74f181b147c8b80FED744B9/task-manager)

## Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 16
- pip

### Database Setup
```bash
# Create the databases
createdb task_manager
createdb task_manager_test

# Seed the database
psql -h 127.0.0.1 task_manager < seeds/task_seeds.sql
```

### Installation
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Database Schema

The application uses two main tables:
- `users`: Stores user information
- `tasks`: Stores task information with foreign key references to users

## Testing

```bash
# Run the tests
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details