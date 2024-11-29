


'''
when I go to / 
I am directed to the home page
'''
def test_slash_sends_do_home(test_web_address, page):
    page.goto(f'http://{test_web_address}/')
    assert page.url == f'http://{test_web_address}/home'