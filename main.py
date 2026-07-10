import requests
import os
from datetime import datetime

token = os.getenv('GH_TOKEN')
headers = {'Authorization': 'Bearer ' + token}

response = requests.get('https://api.github.com/user', headers=headers)

if response.status_code == 200:
    print("Success!")
    user_data = response.json()
    
    # 1. Print simple fields
    print(user_data['login'])
    print("Public repos: ", user_data['public_repos'])
    print("Followers: ", user_data['followers'])
    
    # 2. Use .get() for optional fields to avoid errors
    bio = user_data.get('bio', 'N/A')
    print("Bio: ", bio)
    
    # 3. Parse and format the date
    created_date = datetime.strptime(user_data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = created_date.strftime('%B %d, %Y')
    print("Account created on:", formatted_date)
