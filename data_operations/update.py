# data_operations/update.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country


def update_entry(client):
    try:
        display_countries(client)
        country_code = input("Enter country code: ")
        display_year_for_country(client, country_code)
        year = input("Enter year: ")
        
        print("Current inflation index in dataset: ")
        display_inflation_for_year_country(client,country_code,year)
        new_inflation = input("Enter new inflation index: ")

        query = f"UPDATE theta-cell-406519.inflation_data.gdp_data SET Inflation = {new_inflation} WHERE CountryCode = '{country_code}' AND Year = {year}"

        query_job = client.query(query)
        query_job.result()

        print("Entry Updated")

    except Exception as err:
        print("Error:", err)
