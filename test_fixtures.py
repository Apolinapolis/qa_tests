import pytest



@pytest.fixture()
def user():
    return 'name', 'age'

@pytest.fixture(scope='session')
def browser():
    pass
    yield
    print('tearDown')

@pytest.fixture()
def login_page(browser):
    pass

def test_login(login_page, user):
    assert user[0] == 'name'
    assert user[1] == 'age'

def test_login2(login_page, user):
    assert user[0] == 'name'
    assert user[1] == 'age'