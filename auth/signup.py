# auth/signup.py
from google.cloud import bigquery

def signup(client):
    try:
        username = input("Create your username: ")
        password = input("Create your password: ")

        # Check for uniqueness of user id, this might be a problem later
        query = f"""
            INSERT INTO theta-cell-406519.inflation_data.user_data (Username, Password)
            VALUES ('{username}', '{password}')
        """

        query_job = client.query(query)
        query_job.result()

        # # Fetch the newly created user ID
        # query = f"""
        #     SELECT UserID
        #     FROM theta-cell-406519.inflation_data.user_data
        #     WHERE Username = '{username}' AND Password = '{password}'
        # """

        # query_job = client.query(query)
        # results = query_job.result()

        # user_id = None
        # for row in results:
        #     user_id = row.UserID

        # if user_id:
        print("Signup successful!")
        return {"user": username, "password": password}
    except:
            print("Signup failed. Please try again.")
            return None
