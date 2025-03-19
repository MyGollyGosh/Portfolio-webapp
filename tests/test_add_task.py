from playwright.sync_api import expect

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
    assert description_input.count() == 1
    assert due_date_input.count() == 1
    assert priority_input.count() == 1