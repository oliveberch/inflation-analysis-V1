# data_operations/display_data.py

from google.cloud import bigquery
from prettytable import PrettyTable
import time

def display_countries(client):
    try:
        query = """
            SELECT DISTINCT Country, CountryCode
            FROM theta-cell-406519.inflation_data.country_info
        """

        query_job = client.query(query)
        rows = query_job.result()

        table = PrettyTable()
        table.field_names = ["Country", "Country Code"]

        for row in rows:
            table.add_row([row.Country, row.CountryCode])

        print("\nDistinct Countries and their Codes:\n")
        time.sleep(0.3)
        print(table)

    except Exception as e:
        print(f"Error: {e}")

def display_year_for_country(client, country_code):
    try:
        query = f"""
            SELECT DISTINCT Year
            FROM theta-cell-406519.inflation_data.gdp_data
            WHERE CountryCode = '{country_code}'
        """

        query_job = client.query(query)
        rows = query_job.result()

        table = PrettyTable()
        table.field_names = ["Year"]

        for row in rows:
            table.add_row([row.Year])

        print(f"\nDistinct Years for Country Code {country_code}:\n")
        time.sleep(0.3)
        print(table)

    except Exception as e:
        print(f"Error: {e}")

def display_inflation_for_year_country(client, country_code, year):
    try:
        query = f"""
            SELECT *
            FROM theta-cell-406519.inflation_data.gdp_data
            WHERE CountryCode = '{country_code}' AND Year = {year}
        """

        query_job = client.query(query)
        rows = query_job.result()

        table = PrettyTable()
        table.field_names = ["Country Code", "Year", "Inflation"]

        for row in rows:
            table.add_row([row.CountryCode, row.Year, row.Inflation])
        
        print(f"\nInflation for {country_code} in {year}:\n")
        print(table)
        time.sleep(0.3)

    except Exception as e:
        print(f"Error: {e}")




# from google.cloud import bigquery

# def display_countries(client):
#     # Display distinct countries and their codes
#     query = """
#         SELECT DISTINCT Country, CountryCode
#         FROM theta-cell-406519.inflation_data.country_info
#     """

#     query_job = client.query(query)
#     rows = query_job.result()

#     for row in rows:
#         print(row.values())

# def display_year_for_country(client, country_code):
#     # Display distinct years for a given country
#     query = f"""
#         SELECT DISTINCT Year
#         FROM theta-cell-406519.inflation_data.gdp_data
#         WHERE CountryCode = '{country_code}'
#     """

#     query_job = client.query(query)
#     rows = query_job.result()

#     for row in rows:
#         print(row.values())

# def display_inflation_for_year_country(client, country, year):
#     # Display inflation for a given country and year
#     query = f"""
#         SELECT Inflation
#         FROM theta-cell-406519.inflation_data.gdp_data
#         WHERE CountryCode = '{country}' AND Year = {year}
#     """

#     query_job = client.query(query)
#     rows = query_job.result()

#     for row in rows:
#         print(row.values())
