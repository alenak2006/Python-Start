'''
import requests
import json

response = requests.get('https://randomuser.me/api?results=10')
data = response.json()


for item in data['results']:
    print(item['name']['first'])
'''


def outer():
    def inner():
        return 'inner'
    print(inner())
    return 'outer'


print(outer())
