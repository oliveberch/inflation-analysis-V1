# analysis/view_data.py
from google.cloud import bigquery

def view_data(client, country, start_year, end_year):
    try:
        query = f"SELECT * FROM theta-cell-406519.inflation_data.gdp_data WHERE CountryCode='{country}' AND Year BETWEEN {start_year} AND {end_year}"
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            print(row.CountryCode, row.Year, row.Inflation)

        print("Redirecting to the home page")

    except Exception as e:
        print(f"Error: {e}")
