from lib.task_repository import TaskRepository
from lib.task import Task
from datetime import date

'''
test /add-tasks gets a 200 response
'''
def test_add_tasks_exists(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    response = page.goto(f'http://{test_web_address}/add-task')
    assert response.status == 200

'''
check /add-task page has a box for Description, Due date, priority and to POST the information
'''
def test_required_information_boxes_exist_on_page(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    page.goto(f'http://{test_web_address}/add-task')
    assert page.url == f'http://{test_web_address}/add-task'
    description_input = page.locator('input#description')
    due_date_input = page.locator('input#due-date')
    priority_input = page.locator('input#priority')
    post_button = page.locator('#submit-task')
    assert description_input.count() == 1
    assert due_date_input.count() == 1
    assert priority_input.count() == 1

'''
When I hit submit with valid data, a task is added to my account
'''
def test_valid_submit_adds_task_to_account(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    page.goto(f'http://{test_web_address}/add-task')
    assert page.url == f'http://{test_web_address}/add-task'
    page.fill('input[name=description]', 'First description added')
    page.fill('input[name=due-date]', '2026-01-01')
    page.fill('input[name=priority]', '2')
    page.locator('#submit-task').click()
    repo = TaskRepository(db_connection)
    task = repo.get_by_task_id(5)
    assert task == Task(1, 'First description added', date(2026, 1, 1), task.date_added, 2, 'pending')
