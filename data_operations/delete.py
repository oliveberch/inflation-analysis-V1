# data_operations/delete.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country
import time

def delete_entry(client):
    print("\n+-------------------------------+")
    print("| Welcome to Remove Data Window |")
    print("+-------------------------------+")
    time.sleep(0.5)
    print("\nYou can delete data based on your preferences here!")
    time.sleep(0.5)

    display_countries(client)
    
    country_code = input("\nEnter country code to delete data from: ")
    display_year_for_country(client, country_code)
    year = input("\nEnter year: ")

    try:
        # Delete entry from InflationData
        query = f"""
            DELETE FROM theta-cell-406519.inflation_data.gdp_data
            WHERE CountryCode = '{country_code}' AND Year = {year}
        """

        query_job = client.query(query)
        query_job.result()
        print("\nEntry deleted succesfully")
        time.sleep(1)

    except Exception as e:
        print(f"Error during data deletion: {e}")