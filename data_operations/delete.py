# data_operations/delete.py
from google.cloud import bigquery

def delete_entry(client):
    country = input("Enter country code: ")
    year = input("Enter year: ")

    # Delete entry from InflationData
    query = f"""
        DELETE FROM theta-cell-406519.inflation_data.gdp_data
        WHERE CountryCode = '{country}' AND Year = {year}
    """

    query_job = client.query(query)
    query_job.result()
    print("Entry deleted")
