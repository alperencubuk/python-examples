# Requests Example
import requests
import json
import logging


# Decorator for control response code
def client_method(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return response.json()['results'] if response.status_code == 200 else None
    return wrapper


@client_method
def make_request(count):
    return requests.get(f'https://randomuser.me/api/?results={count}')


def get_users(count):
    data = make_request(count)
    users = []
    for item in data:
        user = {}
        user['title'] = item['name']['title']
        user['first'] = item['name']['first']
        user['last'] = item['name']['last']
        user['username'] = item['login']['username']
        user['password'] = item['login']['password']
        # append user info in users array
        users.append(user)
    # return users in json format
    return json.dumps({'users': users}, indent=4)


if __name__ == "__main__":
    result = get_users(200)
    # write users to json file
    with open('users.json', 'w') as f:
        f.write(result)

    # logging
    logging.basicConfig(
        filename='response.log',
        filemode='w',
        format='%(asctime)s - %(message)s',
        level=logging.INFO)
    logging.info(result)

# Alperen Cubuk
