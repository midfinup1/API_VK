import requests


class User:
    def __init__(self, user_id, domain):
        self.id = user_id
        self.domain = domain
        # self.id = input('Введите id пользователя: ')

    def search_mutual_friends(self, source_uid, target_uid):
        VK_TOKEN = input('Введите токен ВК: ')
        API_BASE_URL = 'https://api.vk.com/method/'
        V = '5.126'
        source_uid = source_user.id
        target_uid = target_user.id
        # self.source_uid = input('Введите id первого пользователя: ')
        # self.target_uid = input('Введите id второго пользователя: ')
        request_url = (API_BASE_URL + 'friends.get')
        response = requests.get(request_url, params={
            'access_token': VK_TOKEN,
            'v': V,
            'user_id': source_uid,
            'fields': 'domain',
            'order': 'name'
        })
        friend_list = {}
        count = response.json()['response']['count']
        for i in range(0, count):
            for friend in response.json()['response']['items']:
                friend_list[friend['id']] = 'https://vk.com/' + friend['domain']
        response = requests.get(request_url, params={
            'access_token': VK_TOKEN,
            'v': V,
            'user_id': target_uid,
            'fields': 'domain',
            'order': 'name'
        })
        mutual_friends = []
        response = response.json()['response']['items']
        temp_list = []
        for i in response:
            temp_list.append(i['id'])
        for friend in friend_list.items():
            if friend[0] in temp_list:
                user = 'user' + str(friend[0])
                mutual_friends.append(user)
                user = User([friend[0]], friend[1])

        print(mutual_friends)


source_user = User(196055093, '')
target_user = User(237127625, '')
source_user.search_mutual_friends(source_user, target_user)
# print(user.domain)

# 196055093
# 237127625
