# data_operations/display_data.py
from google.cloud import bigquery

def display_countries(client):
    # Display distinct countries and their codes
    query = """
        SELECT DISTINCT Country, CountryCode
        FROM theta-cell-406519.inflation_data.country_info
    """

    query_job = client.query(query)
    rows = query_job.result()

    for row in rows:
        print(row.values())

def display_year_for_country(client, country_code):
    # Display distinct years for a given country
    query = f"""
        SELECT DISTINCT Year
        FROM theta-cell-406519.inflation_data.gdp_data
        WHERE CountryCode = '{country_code}'
    """

    query_job = client.query(query)
    rows = query_job.result()

    for row in rows:
        print(row.values())

def display_inflation_for_year_country(client, country, year):
    # Display inflation for a given country and year
    query = f"""
        SELECT Inflation
        FROM theta-cell-406519.inflation_data.gdp_data
        WHERE CountryCode = '{country}' AND Year = {year}
    """

    query_job = client.query(query)
    rows = query_job.result()

    for row in rows:
        print(row.values())
