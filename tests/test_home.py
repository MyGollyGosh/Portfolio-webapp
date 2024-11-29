


'''
when I got to /home
I get a 200 returned
'''
def test_home_page_exists(test_web_address, page):
    response = page.goto(f'http://{test_web_address}/home')
    assert response.status == 200