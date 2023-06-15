#GitUserFetch


This script fetches all users from the GitLab server using the GitLab API. It retrieves the username, name, and email of each user and stores them in a pandas DataFrame. Finally, it exports the data to an Excel file named "gitlab_all_users.xlsx" in the current directory.

Requirements:
-appropriate permissions
-valid personal access token with necessary scope to access the GitLab API as an admin
-gitlab library
-pandas library

Run the following commands in shell to install the libraries:
pip install python-gitlab
pip install pandas