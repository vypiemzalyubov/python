import requests

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.response import Response
# from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post

def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    response_data = Response(response)

    response_data.assert_status_code(200).validate(Post)