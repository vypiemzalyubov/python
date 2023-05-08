from src.baseclasses.response import Response
from src.schemas.post import USERS_SCHEMA
#from src.pydantic_schemas.post import Post

def test_getting_users_list(fixture_get_users):
    Response(fixture_get_users).assert_status_code(200).validate(USERS_SCHEMA)