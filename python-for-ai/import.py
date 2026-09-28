import requests
# to input into the link
username = input('enter a username')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

name = f'Name: {username}'
followers = data['followers']
identity = data['id']


print(name)
print(f'followers: {followers}')
print(f'id: {identity}')