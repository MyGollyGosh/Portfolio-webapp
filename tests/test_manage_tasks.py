from playwright.sync_api import expect

'''
the drop down menu contains all of the users tasks
'''
def test_drop_down_menu_contains_users_tasks(db_connection, test_web_address, page):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    page.goto(f'http://{test_web_address}/manage-tasks')
    assert page.url == f'http://{test_web_address}/manage-tasks'
    task = page.locator('.task-name')
    expect(task.nth(1)).to_have_text('Complete Flask web app project')
    expect(task.nth(2)).to_have_text('Prepare presentation for project')

'''
when I select a task from the drop down menu 
it is displayed on the page
'''
def test_selected_task_is_displayed(db_connection, test_web_address, page):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    page.goto(f'http://{test_web_address}/manage-tasks')
    assert page.url == f'http://{test_web_address}/manage-tasks'
    page.locator('#task').select_option(value='2')
    task = page.locator('.description')
    expect(task).to_have_text('Prepare presentation for project')

# '''
# when I add a new task using the modal form
# it appears in the task list
# '''
# def test_add_task_is_displayed(db_connection, test_web_address, page):
#     db_connection.seed('seeds/task_seeds.sql')
#     page.goto(f'http://{test_web_address}/log-in')
#     page.fill('input[name=uname]', 'johndoe')
#     page.fill('input[name=pwd]', 'Password!1')
#     page.locator('#log-in').click()
#     page.goto(f'http://{test_web_address}/manage-tasks')
#     assert page.url == f'http://{test_web_address}/manage-tasks'
#     page.locator('button:has-text("Add Task")').click()
#     page.fill('input[name=description]', 'Write project documentation')
#     page.fill('input[name=due_date]', '2025-01-15')
#     page.select_option('select[name=priority]', value='3')
#     page.locator('#addTaskForm button[type=submit]').click()
#     page.locator('#task').select_option(value='3')
#     task_list = page.locator('.description')
#     expect(task_list).to_have_text('Write project documentation')
