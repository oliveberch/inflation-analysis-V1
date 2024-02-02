# auth/authenticate.py
from auth.login import login
from auth.signup import signup
import time
from google.cloud import bigquery

def auth_user(client):
    time.sleep(0.5)
    print("\nDo you want to login or sign up? ")
    user_choice = input("\nEnter 'login' or 'signup': ")

    if user_choice.lower() == 'login':
        user_credentials = login(client)
    elif user_choice.lower() == 'signup':
        user_credentials = signup(client)
    else:
        time.sleep(0.5)
        print("\nInvalid choice. Please choose either to 'login' or 'signup'.")
        return None

    if user_credentials == "OK":
        time.sleep(0.5)
        print("\n+---------------------------------+")
        print("| User authentication successful! |")
        print("+---------------------------------+")
        time.sleep(0.5)
        return user_credentials
    else:
        # print("Do you want to try again or exit?")
        # choice = input("Enter try or exit: ")
        # if choice.lower() == "try":
        #     if user_choice.lower() == 'login':
        #         user_credentials = login(client)
        #     elif user_choice.lower() == 'signup':
                # user_credentials = signup(client)
        # else:
            print("\n+-----------------------------+")
            print("| User authentication failed. |")
            print("+-----------------------------+")
            time.sleep(0.5)
            return None
