# data_operations/create.py

from google.cloud import bigquery
import time

def create_entry(client):
    print("\n+----------------------------+")
    print("| Welcome to Add Data Window |")
    print("+----------------------------+")
    time.sleep(0.5)
    try:
        country = input("\nEnter country name you want to add: ")
        country_code = input(f"Enter country code for {country}: ")
        year = input("Enter year of data record: ")
        inflation = input(f"Enter inflation index for {year}: ")

        # Check if the entry already exists in CountryInfo
        query_country_info = f"""
            SELECT COUNT(*) as count
            FROM theta-cell-406519.inflation_data.country_info
            WHERE CountryCode = '{country_code}'
        """
        result_country_info = client.query(query_country_info).result()

        count_country_info = None
        for row in result_country_info:
            count_country_info = row['count']

        if count_country_info == 0:
            # Entry doesn't exist, insert into CountryInfo
            query_insert_country_info = f"""
                INSERT INTO theta-cell-406519.inflation_data.country_info (CountryCode, Country)
                VALUES ('{country_code}', '{country}')
            """
            client.query(query_insert_country_info).result()

        # Check if the entry already exists in InflationData
        query_inflation_data = f"""
            SELECT COUNT(*) as count
            FROM theta-cell-406519.inflation_data.gdp_data
            WHERE CountryCode = '{country_code}' AND Year = {year}
        """
        result_inflation_data = client.query(query_inflation_data).result()

        count_inflation_data = None
        for row in result_inflation_data:
            count_inflation_data = row['count']

        if count_inflation_data == 0:
            # Entry doesn't exist, insert into InflationData
            query_insert_inflation_data = f"""
                INSERT INTO theta-cell-406519.inflation_data.gdp_data (CountryCode, Year, Inflation)
                VALUES ('{country_code}', {year}, {inflation})
            """
            client.query(query_insert_inflation_data).result()
        else:
            # Entry already exists, update the Inflation value
            print(".\n"*5)
            query_update_inflation_data = f"""
                UPDATE theta-cell-406519.inflation_data.gdp_data
                SET Inflation = {inflation}
                WHERE CountryCode = '{country_code}' AND Year = {year}
            """
            client.query(query_update_inflation_data).result()

        print("\nData Added successfully")
        time.sleep(1)

    except Exception as e:
        print(f"Encountered Error: {e}")


# from google.cloud import bigquery

# def create_entry(client):

#     country = input("Enter country name: ")
#     country_code = input("Enter country code: ")
#     year = input("Enter year: ")
#     inflation = input("Enter inflation index: ")

#     # Check if the entry already exists in CountryInfo
#     query = f"""
#         SELECT COUNT(*) as count
#         FROM theta-cell-406519.inflation_data.country_info
#         WHERE CountryCode = '{country_code}'
#     """

#     query_job = client.query(query)
#     result = query_job.result()
#     count = result[0].count

#     if count == 0:
#         # Entry doesn't exist, insert into CountryInfo
#         query = f"""
#             INSERT INTO theta-cell-406519.inflation_data.country_info (CountryCode, Country)
#             VALUES ('{country_code}', '{country}')
#         """
#         query_job = client.query(query)
#         query_job.result()

#     # Check if the entry already exists in InflationData
#     query = f"""
#         SELECT COUNT(*) as count
#         FROM theta-cell-406519.inflation_data.gdp_data
#         WHERE CountryCode = '{country_code}' AND Year = {year}
#     """

#     query_job = client.query(query)
#     result = query_job.result()
#     count = result[0].count

#     if count == 0:
#         # Entry doesn't exist, insert into InflationData
#         query = f"""
#             INSERT INTO theta-cell-406519.inflation_data.gdp_data (CountryCode, Year, Inflation)
#             VALUES ('{country_code}', {year}, {inflation})
#         """
#     else:
#         # Entry already exists, update the Inflation value
#         print(".\n"*5)
#         query = f"""
#             UPDATE theta-cell-406519.inflation_data.gdp_data
#             SET Inflation = {inflation}
#             WHERE CountryCode = '{country_code}' AND Year = {year}
#         """

#     query_job = client.query(query)
#     query_job.result()
#     print("Data Added successfully")
