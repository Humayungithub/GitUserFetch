import gitlab
import pandas as pd

# GitLab API endpoint and personal access token
gitlab_url = 'https://gitlab.example.com'  # Replace with your GitLab URL
access_token = 'YOUR_PERSONAL_ACCESS_TOKEN'  # Replace with your personal access token

# Initialize GitLab instance
gl = gitlab.Gitlab(gitlab_url, private_token=access_token)

# Fetch all users in GitLab server
users = gl.users.list(all=True)

# Prepare data for Excel
data = []
for user in users:
    username = user.username
    name = user.name
    email = user.email
    data.append([username, name, email])

# Create DataFrame and export to Excel
df = pd.DataFrame(data, columns=['Username', 'Name', 'Email'])
df.to_excel('gitlab_all_users.xlsx', index=False)
