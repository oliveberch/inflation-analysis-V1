from google.cloud import bigquery
from google.oauth2 import service_account

import time

from auth.authenticate import auth_user

from data_operations.create import create_entry
from data_operations.read import read_entries
from data_operations.update import update_entry
from data_operations.delete import delete_entry

from analysis.analysis_flow import analysis_flow

credentials = service_account.Credentials.from_service_account_file('theta-cell-406519-f072918cb9bd.json')

def main():
    # Connect to Google BigQuery
    # client = bigquery.Client()
    client = bigquery.Client(credentials=credentials)

    print("\n+----------------------------------------+")
    print("| Welcome to the Inflation Analysis App! |")
    print("+----------------------------------------+")
    try:
        # Authenticate user
        user_credentials = auth_user(client)

        if user_credentials != "OK":
            print("\n+-------------------------------------+")
            print("| Exiting the Inflation Analysis App. |")
            print("+-------------------------------------+")
        else:
            # Inflation insight home page
            while True:
                print("\n+----------------------+")
                print("| Welcome to Home page |")
                print("+----------------------+")
                time.sleep(0.5)
                print("\nHow can we help you? ")
                print("1. Add Data")
                print("2. Read Data")
                print("3. Update Data")
                print("4. Delete Data")
                print("5. Analyse Data")
                print("6. Exit App")

                user_choice = input("\nEnter your choice (1-6): ")

                if user_choice == "1":
                    create_entry(client)
                elif user_choice == "2":
                    read_entries(client)
                elif user_choice == "3":
                    update_entry(client)
                elif user_choice == "4":
                    delete_entry(client)
                elif user_choice == "5":
                    analysis_flow(client)
                elif user_choice == "6":
                    print("\n+----------------------------------------------+")
                    print("| Exiting the Inflation Analysis App. Goodbye! |")
                    print("+----------------------------------------------+")
                    break
                else:
                    print("\n+--------------------------------------------------------+")
                    print("| Invalid choice. Please enter a number between 1 and 6. |")
                    print("+--------------------------------------------------------+")

    except Exception as e:
        print(f"Encountered Error: {e}")

if __name__ == "__main__":
    main()