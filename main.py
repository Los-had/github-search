import requests
import json
from time import sleep

def main():
  while True:
    search_user_name = input('What user do you want to search?\n >  ')
    github = requests.get(f'https://api.github.com/users/{search_user_name}')
    response = json.loads(github.text)
    if 'message' in response:
      print('User not found!')
      sleep(10)
      break
    bio = response['bio'].replace('\r\n', '')
    name = response['name']
    username = response['login']
    followers = response['followers']
    follwoing = response['following']
    site = response['blog']
    email = response['email']
    if email == None:
      email = "Don't have a public email"
    hireable = response['hireable']
    if hireable == None:
      hireable = 'Not hireable'
    twitter_username = response['twitter_username']
    location = response['location']
    company = response['company']
    print(f'\n----------------------------------------------\n{username}\n----------------------------------------------\nname: {name}\ndescription: {bio}\nemail: {email}\nwebsite: {site}\nfollowers: {str(followers)}\nfollowing: {str(follwoing)}\ntwitter username: {twitter_username}\ncompany: {company}\nhireable: {hireable}\nlocation: {location}\nprofile link: https://github.com/{username}\n----------------------------------------------')

if __name__ == '__main__':
  main()