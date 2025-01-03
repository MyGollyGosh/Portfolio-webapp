from playwright.sync_api import expect

'''
the drop down menu on contains all of the users tasks
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