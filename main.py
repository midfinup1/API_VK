from urllib.parse import urlencode
import requests


class User:
    def __init__(self, token: str):
        self.token = input('Введите токен ВК: ')

    def search_mutual_friends(self, source_uid, target_uid):
        VK_TOKEN = self.token
        API_BASE_URL = 'https://api.vk.com/method/'
        V = '5.126'
        print(VK_TOKEN)
        source_uid = input('Введите id первого пользователя: ')
        target_uid = input('Введите id второго пользователя: ')
        request_url = (API_BASE_URL + 'friends.getMutual')
        response = requests.get(request_url, params={
            'access_token': VK_TOKEN,
            'v': V,
            'source_uid': source_uid,
            'target_uid': target_uid,
        })
        print(response.json())


user = User('')
user.search_mutual_friends('', '')


# 226338816
# 237127625

