# auth/login.py
from google.cloud import bigquery

def login(client):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    query = f"""
        SELECT COUNT(*) as user_count
        FROM theta-cell-406519.inflation_data.user_data
        WHERE Username = '{username}' AND Password = '{password}'
    """

    query_job = client.query(query)
    results = query_job.result()

    for row in results:
        user_count = row.user_count

    if user_count > 0:
        print("Login successful!")
        return {"user": username, "password": password}
    else:
        print("Login failed. Please check your credentials.")
        return None
