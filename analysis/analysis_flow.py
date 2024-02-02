# analysis/analysis_flow.py
from analysis.user_input import country, year
from analysis.view_data import view_data
from analysis.visualize import filter_data, plot_inflation_line, plot_inflation_bar
import time

def analysis_flow(client):
    user_country = country(client)
    user_start_year, user_end_year = year(client, user_country)
    
    user_analysis_prefence = input("Enter your data analysis preference (e.g., 'data', 'visual', etc.): ")

    if user_analysis_prefence == 'data':
        
        print("\n+---------------------------+")
        print("| Welcome to Data Dashboard |")
        print("+---------------------------+")
        time.sleep(0.5)
        print("\nRetriving inflation records..\n")
        view_data(client, user_country, user_start_year, user_end_year)
        print("\nData range displayed. Exiting analysis page.")
        time.sleep(0.5)

    elif user_analysis_prefence == 'visual':
        print("+------------------------------------+")
        print("| Welcome to Visualization Dashboard |")
        print("+------------------------------------+")

        user_visual_preference = input("\nEnter your visualization preference (e.g., 'plot', 'bar', etc.): ")
        print("\nGtting your analysis ready in new window.. Close window to return to App\n")
        time.sleep(0.3)

        if user_visual_preference == 'plot':
            filtered_data = filter_data(client, user_country, user_start_year, user_end_year)
            plot_inflation_line(filtered_data)
            print("\nData range visualized. Exiting analysis page.")
            time.sleep(0.5)

        elif user_visual_preference == 'bar':
            filtered_data = filter_data(client, user_country, user_start_year, user_end_year)
            plot_inflation_bar(filtered_data)
            print("\nData range visualized. Exiting analysis page.")
            time.sleep(0.5)

        else:
            print("\nInvalid preference. Exiting analysis page.")
