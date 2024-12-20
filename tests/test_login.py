from playwright.sync_api import expect


'''
when I got to /log-in 
I get a 200 response
'''
def test_log_in_exists(test_web_address, page):
    response = page.goto(f'http://{test_web_address}/log-in')
    assert response.status == 200

'''
when I click the log in button with valid credentials
I am redirected to the home page
'''
def test_successful_log_in_directs_to_home_page(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'

'''
When I click the log in button with invalid credentials
I get an error message that states invalid credentials
'''
def test_invalid_credentials_shows_invalid_message(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Passw')
    page.locator('#log-in').click()
    error_message = page.locator('.log_in_message')
    expect(error_message).to_have_text('Invalid username or password')

'''
When I click on the sign up button
I am taken to the /sign_up page
'''
def test_sign_up_button_directs_to_sign_up_page(test_web_address, page):
    page.goto(f'http://{test_web_address}/log-in')
    page.locator('.sign-up').click()
    assert page.url == f'http://{test_web_address}/sign-up'

'''
When I click the home button on /log-in
I am directed to the home page
'''
def test_home_button_on_log_in_page_directs_to_home_page(test_web_address, page):
    page.goto(f'http://{test_web_address}/log-in')
    page.locator('.home').click()
    assert page.url == f'http://{test_web_address}/home'

'''
when I am on the login page
I see a login button    
'''
def test_guest_sees_login_button(test_web_address, page):
    page.goto(f'http://{test_web_address}/home')
    auth_button = page.locator('.log-in')
    expect(auth_button).to_have_text('login')

'''
when I am logged in
I cannot access /login
I am redifected to home
'''
def test_logged_in_user_cannot_acces_login_page_redirected_to_home(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    page.goto(f'http://{test_web_address}/log-in')
    assert page.url == f'http://{test_web_address}/home'
    assert page.locator('.log-in-form').count() == 0
