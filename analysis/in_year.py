# analysis/in_year.py
from google.cloud import bigquery
from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country

def year(client, country_code):
    try:
        # query = f"SELECT DISTINCT Year FROM theta-cell-406519.inflation_data.gdp_data WHERE CountryCode='{country}'"
        # query_job = client.query(query)
        # results = query_job.result()

        # for row in results:
        #     print(row.Year)
        
        display_year_for_country(client, country_code)

        start_year = input("Enter the start year: ")
        end_year = input("Enter the end year: ")

        return start_year, end_year

    except Exception as e:
        print(f"Error: {e}")
        return None, None
