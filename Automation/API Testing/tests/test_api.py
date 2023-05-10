import pytest
from src.baseclasses.response import Response
from src.schemas.post import USERS_SCHEMA
#from src.pydantic_schemas.post import Post

@pytest.mark.prod
def test_getting_users_list(fixture_get_users):
    """
    Try to check status code is 200 and validate response json
    """    
    Response(fixture_get_users).assert_status_code(200).validate(USERS_SCHEMA)


@pytest.mark.dev
@pytest.mark.skip('Test skip')
def test_something_1():
    """
    Try to check 1 is equal to 1
    """
    assert 1 == 1

@pytest.mark.dev
def test_something_2():
    """
    Try to check 1 is equal to 1
    """    
    assert 1 == 1    

@pytest.mark.dev
def test_something_3():
    """
    Try to check 1 is equal to 2
    """    
    assert 1 == 2    