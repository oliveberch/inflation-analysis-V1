# auth/authenticate.py
from auth.login import login
from auth.signup import signup
from google.cloud import bigquery

def auth_user(client):
    user_choice = input("Do you want to login or sign up? Enter 'login' or 'signup': ")

    if user_choice.lower() == 'login':
        user_credentials = login(client)
    elif user_choice.lower() == 'signup':
        user_credentials = signup(client)
    else:
        print("Invalid choice. Please enter 'login' or 'signup'.")
        return None

    if user_credentials:
        print("User authentication successful!")
        return user_credentials
    else:
        print("User authentication failed.")
        return None
