import requests
import os
from datetime import datetime

token = os.getenv('GH_TOKEN')
headers = {'Authorization': 'Bearer ' + token}

response = requests.get('https://api.github.com/user', headers=headers)

if response.status_code == 200:
    user_data = response.json()
    
    # Prepare the formatted string
    created_date = datetime.strptime(user_data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = created_date.strftime('%B %d, %Y')
    
    # Create the markdown content
    content = f"""# GitHub Profile Report
- **Username:** {user_data['login']}
- **Public repos:** {user_data['public_repos']}
- **Followers:** {user_data['followers']}
- **Bio:** {user_data.get('bio', 'N/A')}
- **Account created on:** {formatted_date}
"""
    
    # Save to a file
    with open('PROFILE.md', 'w') as f:
        f.write(content)
        
    print("Report generated successfully!")
