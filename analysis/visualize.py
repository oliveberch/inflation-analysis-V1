# analysis/visualize.py
import pandas as pd
import matplotlib.pyplot as plt

def filter_data(client, country=None, start_year=None, end_year=None):
    try:
        query = "SELECT * FROM theta-cell-406519.inflation_data.gdp_data WHERE 1=1"

        if country:
            query += f" AND CountryCode='{country}'"
        if start_year and end_year:
            query += f" AND Year BETWEEN {start_year} AND {end_year}"
        elif start_year:
            query += f" AND Year >= {start_year}"
        elif end_year:
            query += f" AND Year <= {end_year}"

        query_job = client.query(query)
        results = list(query_job.result())

        for row in results:
            print(row.CountryCode, row.Year, row.Inflation)

        return pd.DataFrame(results, columns=['CountryCode', 'Year', 'Inflation'])

    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame(columns=['CountryCode', 'Year', 'Inflation'])


def plot_inflation_line(data):
    plt.plot(data['Year'], data['Inflation'], marker='o')
    plt.title(f'Inflation Trend for {data["CountryCode"].iloc[0]} ({data["Year"].min()} to {data["Year"].max()})')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.show()

def plot_inflation_bar(data):
    plt.bar(data['Year'], data['Inflation'])
    plt.title(f'Inflation Bar Chart for {data["CountryCode"].iloc[0]} ({data["Year"].min()} to {data["Year"].max()})')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.show()


# def filter_data(client, country=None, start_year=None, end_year=None):
#     try:
#         query = f"SELECT * FROM theta-cell-406519.inflation_data.gdp_data WHERE "

#         if country:
#             query += f" AND CountryCode='{country}'"
#         if start_year:
#             query += f" AND Year>={start_year}"
#         if end_year:
#             query += f" AND Year<={end_year}"

#         query_job = client.query(query)
#         results = query_job.result()

#         data = []
#         for row in results:
#             data.append(row)

#         return pd.DataFrame(data, columns=['CountryCode', 'Year', 'Inflation'])

#     except Exception as e:
#         print(f"Error: {e}")
#         return pd.DataFrame()