# auth/signup.py
from google.cloud import bigquery

def signup(client):
    print("\n+--------------------------+")
    print("| Welcome to signup window |")
    print("+--------------------------+")
    try:
        username = input("\nCreate your username: ")
        password = input("Create your password: ")

        # Check for uniqueness of user id, this might be a problem later
        query = f"""
            INSERT INTO theta-cell-406519.inflation_data.user_data (Username, Password)
            VALUES ('{username}', '{password}')
        """

        query_job = client.query(query)
        query_job.result()

        print("\n+--------------------+")
        print("| Signup successful! |")
        print("+--------------------+")
        return "OK"
    except:
            print("\n+----------------------------------+")
            print("| Signup failed. Please try again. |")
            print("+----------------------------------+")
            return None
