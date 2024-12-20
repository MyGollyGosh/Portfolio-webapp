from playwright.sync_api import expect


'''
test /tasks get 200 response
'''
def test_tasks_exists(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    response = page.goto(f'http://{test_web_address}/tasks')
    assert response.status == 200

'''
when I am on the tasks page as an authenticated user
I see the logout button
'''
def test_logout_button_exists_for_logged_in_user(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    page.goto(f'http://{test_web_address}/tasks')
    auth_button = page.locator('.logout')
    expect(auth_button).to_have_text('logout')

'''
When I am not logged in, if I attempt to access /tasks
I am redirected to /login
'''
def test_guest_user_accessing_tasks_is_directed_to_login_page(test_web_address, page):
    page.goto(f'http://{test_web_address}/tasks')
    assert page.url == f'http://{test_web_address}/log-in'

'''
When I am logged in, if I attempt to access /tasks
I am directed to /tasks
'''
def test_logged_in_user_is_able_to_view_tasks(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    page.goto(f'http://{test_web_address}/tasks')
    assert page.url == f'http://{test_web_address}/tasks'
