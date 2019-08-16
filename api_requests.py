# Requests Example
import requests
import json
import logging


# Decorator for control response code
def client_method(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return response.json() if response.status_code == 200 else None
    return wrapper


@client_method
def make_request(count):
    return requests.get(f'https://randomuser.me/api/?results={count}')


def get_users(count):
    data = make_request(count)
    users = []
    for i in range(count):
        user = {}
        # title, first and last are optional
        user['title'] = data.get('results')[i].get('name').get('title')
        user['first'] = data.get('results')[i].get('name').get('first')
        user['last'] = data.get('results')[i].get('name').get('last')
        # username and password are required
        user['username'] = data['results'][i]['login']['username']
        user['password'] = data['results'][i]['login']['password']
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
