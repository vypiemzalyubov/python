import requests


response = requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=True)
first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)




# from json.decoder import JSONDecodeError
# import requests


# response = requests.get('https://playground.learnqa.ru/api/get_text')
# print(response.text)

# try:
#     parsed_response = response.json()
#     print(parsed_response)
# except JSONDecodeError:
#     print("Response is not JSON format")