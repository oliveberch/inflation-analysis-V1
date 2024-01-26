# analysis/in_country.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country

def country(client):
    try:
        # query = "SELECT DISTINCT CountryCode FROM theta-cell-406519.inflation_data.gdp_data"
        
        # query_job = client.query(query)
        # results = query_job.result()

        # for row in results:
        #     print(row.CountryCode)

        display_countries(client)
        
        country_code = input("Enter the country code: ")
        return country_code

    except Exception as e:
        print(f"Error: {e}")
        return None
