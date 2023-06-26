import gitlab
import pandas as pd

# GitLab API endpoint and personal access token
gitlab_url = 'https://gitlab.example.com'  # Replace with your GitLab URL
access_token = 'YOUR_PERSONAL_ACCESS_TOKEN'  # Replace with your personal access token

# Initialize GitLab instance
gl = gitlab.Gitlab(gitlab_url, private_token=access_token)

# ID or path of the GitLab group
group_id = 'your_group_id'  # Replace with the ID or path of your GitLab group

# Fetch all group members
group = gl.groups.get(group_id)
members = group.members.list(all=True)

# Prepare data for Excel
data = []
for member in members:
    user = member.attributes['username']
    email = member.attributes['email']
    name = member.attributes['name']
    data.append([user, email, name])

# Create DataFrame and export to Excel
df = pd.DataFrame(data, columns=['Username', 'Email', 'Name'])
df.to_excel('gitlab_group_users.xlsx', index=False)