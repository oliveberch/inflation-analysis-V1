# data_operations/read.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country

def read_entries(client):
    print("Read data from BigQuery based on your preferences.")

    display_countries(client)
    country_code = input("Enter country code: ")

    display_year_for_country(client, country_code)
    start_year = input("Enter Start year: ")
    end_year = input("Enter End year: ")

    query = f"SELECT * FROM theta-cell-406519.inflation_data.gdp_data WHERE "
    params = []

    if country_code:
        query += f"CountryCode = '{country_code}'"
        params.append(country_code)

    if start_year:
        query += f" AND Year >= {start_year}"
        params.append(start_year)

    if end_year:
        query += f" AND Year <= {end_year}"
        params.append(end_year)

    # Remove the trailing "AND" if any
    if query.endswith("AND"):
        query = query[:-4]

    query_job = client.query(query)
    rows = query_job.result()

    # Display the data
    for row in rows:
        print(row.values())

    print("Exiting Read Data Page")
    return
