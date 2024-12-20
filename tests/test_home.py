from playwright.sync_api import expect


'''
when I got to /home
I get a 200 returned
'''
def test_home_page_exists(test_web_address, page):
    response = page.goto(f'http://{test_web_address}/home')
    assert response.status == 200

'''
when I am on the home page and not logged in
the welcome message says guest
'''
def test_welcome_message_greets_as_guest_when_not_logged_in(test_web_address, page):
    page.goto(f'http://{test_web_address}/home')
    greeting = page.locator('.greeting')
    expect(greeting).to_have_text('Welcome, Guest!')

'''
when I am on the home page and logged in
the welcome message says my name
'''
def test_welcome_message_customises_for_username(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    greeting = page.locator('.greeting')
    expect(greeting).to_have_text('Welcome, johndoe!')

'''
when I am on the home page as a guest
I see a login button
'''
def test_guest_sees_login_button(test_web_address, page):
    page.goto(f'http://{test_web_address}/home')
    auth_button = page.locator('.log-in')
    expect(auth_button).to_have_text('login')

'''
when I am on the home page as an authenticated user
I see the logout button
'''
def test_logout_button_exists_for_logged_in_user(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    auth_button = page.locator('.logout')
    expect(auth_button).to_have_text('logout')

