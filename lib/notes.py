import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

def notes():
    print('Welcome to the Notes App!')






notes()