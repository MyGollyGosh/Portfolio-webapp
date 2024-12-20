


'''
When I click the logout button
I am redirected to the the login page
'''
def test_logout_redirects_to_login_page(test_web_address, page, db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    page.goto(f'http://{test_web_address}/log-in')
    page.fill('input[name=uname]', 'johndoe')
    page.fill('input[name=pwd]', 'Password!1')
    page.locator('#log-in').click()
    assert page.url == f'http://{test_web_address}/home'
    page.locator('.logout').click()
    assert page.url == f'http://{test_web_address}/log-in'

