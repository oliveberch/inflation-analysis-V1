# analysis/view_data.py

from google.cloud import bigquery
from prettytable import PrettyTable
import time

def view_data(client, country_code, start_year, end_year):
    try:
        query = f"SELECT * FROM theta-cell-406519.inflation_data.gdp_data WHERE CountryCode='{country_code}' AND Year BETWEEN {start_year} AND {end_year}"
        query_job = client.query(query)
        results = query_job.result()

        # Fetch country name if results exist
        country_query = f"SELECT Country FROM theta-cell-406519.inflation_data.country_info WHERE CountryCode='{country_code}'"
        country_result = client.query(country_query).result()
        country_name = list(country_result)[0].Country if country_result.total_rows > 0 else "Unknown"

        # Create a PrettyTable instance
        table = PrettyTable()
        table.field_names = ["Country Code", "Year", "Inflation"]

        # Populate the table with data
        for row in results:
            table.add_row([row.CountryCode, row.Year, row.Inflation])

        # Print the table
        print(f"\nInflation Data for {country_name} from {start_year} to {end_year}")
        time.sleep(0.5)
        print(table)

        print("\nRedirecting to the home page")
        time.sleep(0.5)

    except Exception as e:
        print(f"\nError with displaying data: {e}")


# from google.cloud import bigquery

# def view_data(client, country_code, start_year, end_year):
#     try:
#         query = f"SELECT * FROM theta-cell-406519.inflation_data.gdp_data WHERE CountryCode='{country_code}' AND Year BETWEEN {start_year} AND {end_year}"
#         query_job = client.query(query)
#         results = query_job.result()

#         country = f"SELECT Country FROM theta-cell-406519.inflation_data.country_info
#                      WHERE CountryCode='{country_code}'"
        


#         for row in results:
#             print(row.CountryCode, row.Year, row.Inflation)

#         print("Redirecting to the home page")

#     except Exception as e:
#         print(f"Error: {e}")

