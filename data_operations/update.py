# data_operations/update.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country
import time


def update_entry(client):
    try:
        print("\n+-------------------------------+")
        print("| Welcome to Modify Data Window |")
        print("+-------------------------------+")
        time.sleep(0.5)
        print("\nYou can read data based on your preferences here!")
        time.sleep(0.5)

        display_countries(client)
        country_code = input("\nEnter country code to modify: ")

        display_year_for_country(client, country_code)
        year = input("\nEnter year: ")
        
        print("\nCurrent inflation index in dataset: ")
        display_inflation_for_year_country(client,country_code,year)

        new_inflation = input("\nEnter new inflation index: ")

        query = f"UPDATE theta-cell-406519.inflation_data.gdp_data SET Inflation = {new_inflation} WHERE CountryCode = '{country_code}' AND Year = {year}"

        query_job = client.query(query)
        query_job.result()

        print("\nEntry Updated")

    except Exception as err:
        print("\nError:", err)
