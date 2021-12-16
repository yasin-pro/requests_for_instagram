import requests
import json
from datetime import datetime

# start script for login with request

username = '***'
password = '***'

link  = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())
response = requests.get(link)
csrf = response.cookies['csrftoken']

payload = {
	'username': username,
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
	'queryParams': {},
	'optIntoOneTap': 'false'
}

# please edit user agent 
login_header = {
	"User-Agent": "***",
	"X-Requested-With": "XMLHttpRequest",
	"Referer": "https://www.instagram.com/accounts/login/",
	"x-csrftoken": csrf
}

login_response = requests.post(login_url , data = payload , headers = login_header)

json_data = json.loads(login_response.text)

if json_data['authenticated']: 
	print('Login is successfuly!')
else : 
	print('Your login proccess is failed!')

# end script for login with requests


