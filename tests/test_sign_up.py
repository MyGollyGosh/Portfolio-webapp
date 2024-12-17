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
I get an appropriate error
'''
def test_sign_up_with_invalid_username_gives_error(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/sign-up')
    page.fill('input[name=uname]', ' ')
    page.fill('input[name=email]', 'lachlan@mail.com')
    page.fill('input[name=psw]', 'Password!1')
    page.locator('#sign-up-button').click()
    assert page.url == f'http://{test_web_address}/sign-up'
    