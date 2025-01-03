from lib.user_repository import UserRepository


'''
when I go to /sign-up
I get a 200 response
'''
def test_sign_up_page_exists(test_web_address, page):
    response = page.goto(f'http://{test_web_address}/sign-up')
    assert response.status == 200

'''
when I click the sign up button with valid credentials
a user is added to the DB and I am directed to the home page
'''
def test_sign_up_with_valid_credentials_adds_to_db_and_directs_to_home(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = UserRepository(db_connection)
    page.goto(f'http://{test_web_address}/sign-up')
    page.fill('input[name=uname]', 'lachlan')
    page.fill('input[name=email]', 'lachlan@mail.com')
    page.fill('input[name=psw]', 'Password!1')
    page.locator('#sign-up-button').click()
    assert repo.validate_user('lachlan', 'Password!1')
    assert page.url == f'http://{test_web_address}/home'

'''
when I click the sign up button with an invalid username
I get am not able to create an account
'''
def test_sign_up_with_invalid_username_gives_error(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/sign-up')
    page.fill('input[name=uname]', ' ')
    page.fill('input[name=email]', 'lachlan@mail.com')
    page.fill('input[name=psw]', 'Password!1')
    page.locator('#sign-up-button').click()
    assert page.url == f'http://{test_web_address}/sign-up'
    
'''
when I click the home button
I am directed to the home page
'''
def test_home_button_on_sign_up_page_directs_correctly(test_web_address, page):
    page.goto(f'http://{test_web_address}/sign-up')
    page.locator('.home').click()
    assert page.url == f'http://{test_web_address}/home'

'''
when I am logged in and try to access /sign-up
I am redirected to /home
'''
def test_logged_in_user_accessing_sign_up_is_directed_to_home(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    page.goto(f'http://{test_web_address}/sign-up')
    assert page.url == f'http://{test_web_address}/home'

'''
when I am not logged in
I am able to access /sign-up
'''
def test_guest_user_can_access_sign_up(test_web_address, page):
    page.goto(f'http://{test_web_address}/sign-in')
    assert page.url == f'http://{test_web_address}/sign-in'