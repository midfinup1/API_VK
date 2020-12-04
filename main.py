import requests


class User:

    def __init__(self, token, user_id=''):
        self.token = token
        self.user_id = user_id

    def __and__(self, other):
        resp1 = self.get_friends()
        resp2 = other.get_friends()
        common = []
        for item in resp1['response']['items']:
            if item in resp2['response']['items']:
                common.append(item)
        return common

    def get_status(self):
        response = requests.get(
            'https://api.vk.com/method/status.get',
            params={
                'access_token': self.token,
                'v': 5.103
            }
        )
        return response.json()

    def set_status(self, text):
        response = requests.get(
            'https://api.vk.com/method/status.set',
            params={
                'access_token': self.token,
                'v': 5.103,
                'text': text
            }
        )
        return response.json()

    def __repr__(self):
        return 'https://vk.com/id' + str(self.user_id)

    def get_friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'v': 5.103,
                'user_id': self.user_id
            }
        )
        return response.json()

TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
Anna = User(TOKEN, '196055093')
Petya = User(TOKEN, '237127625')
print(Anna & Petya)
print(Anna)
print(Petya)


# 196055093
# 237127625
