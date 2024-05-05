import os
import yfinance as yf
import pandas as pd
import sqlite3

# Pull data
def pull_data():
    company_tickers = ['AXP', 'BCS', 'HSBC', 'LYG', 'VANQ.L', 'COF-PK']
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    dataframes = []

    for ticker_symbol in company_tickers:
        ticker = yf.Ticker(ticker_symbol)
        historical_data = ticker.history(start=start_date, end=end_date)
        historical_data['Ticker'] = ticker_symbol
        dataframes.append(historical_data)

    combined_frames = pd.concat(dataframes)
    return combined_frames

# Save data to CSV
def save_to_csv(output_dir):
    csv_file_path = os.path.join(output_dir, 'historical_data.csv')
    pull_data().to_csv(csv_file_path)

# Convert data to SQL
def convert_to_sql(input_csv_path):
    try:
        connection = sqlite3.connect('historical_data.db')
        dfs = pd.read_csv(input_csv_path)
        dfs.to_sql('historical_data', connection, if_exists='replace', index=False)
    except Exception as e:
        print(f"An error occurred in connection within convert_to_sql: {e}")
    finally:
        connection.close()

# Execute SQL query
def execute_query(query):
    connection = sqlite3.connect('historical_data.db')
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()

# Main function to execute SQL queries
def main():
    query1 = (
        "SELECT Ticker, MAX(High) AS Highest_Stock_Sale_2023 "
        "FROM historical_data "
        "GROUP BY Ticker")
    execute_query(query1)
    query2 = (
        "SELECT Ticker, Min(Low) AS Lowest_Stock_Sale_2023 "
        "FROM historical_data "
        "GROUP BY Ticker")
    execute_query(query2)

if __name__ == "__main__":
    output_directory = input("Enter the directory path to save the files: ").strip()
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    save_to_csv(output_directory)
    input_csv_path = os.path.join(output_directory, 'historical_data.csv')
    convert_to_sql(input_csv_path)
    main()  # Execute SQL queries and print to terminal
