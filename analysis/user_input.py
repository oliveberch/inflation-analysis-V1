# analysis/user_input.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country

def country(client):
    try:
        print("\n+-----------------------------------+")
        print("| Countries for which we have data: |")
        print("+-----------------------------------+")

        display_countries(client)
        
        country_code = input("\nEnter the country code you want analysis for: ")
        return country_code

    except Exception as e:
        print(f"Error: {e}")
        return None

def year(client, country_code):
    try:
        # fetch country name
        country_query = f"SELECT Country FROM theta-cell-406519.inflation_data.country_info WHERE CountryCode='{country_code}'"
        country_result = client.query(country_query).result()
        country_name = list(country_result)[0].Country
        

        print(f"\nYears for which we have data on {country_name} : ")
        
        display_year_for_country(client, country_code)

        start_year = input("\nEnter the start year: ")
        end_year = input("\nEnter the end year: ")

        return start_year, end_year

    except Exception as e:
        print(f"Error: {e}")
        return None, None