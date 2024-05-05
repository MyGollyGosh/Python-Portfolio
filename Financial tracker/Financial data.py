import yfinance as yf
import pandas as pd
import sqlite3

#pull data
def pull_data():
    #AXP = American Express, BCS = Barclays, HSBC = HSBC, LYG = Llyods VANQ = Vanquis COF-PK = Capital One
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

#save data to CSV
def save_to_csv():
    csv_file_path = 'C:\\Users\\64Bit 120GB SSD\\Desktop\\Financial tracker\\historical_data.csv'
    pull_data().to_csv(csv_file_path)

#convert data to SQL
def convert_to_sql():
    try:
        connection = sqlite3.connect('historical_data.db')
        dfs = pd.read_csv('C:\\Users\\64Bit 120GB SSD\\Desktop\\Financial tracker\\historical_data.csv')
        dfs.to_sql('historical_data', connection, if_exists='replace', index=False)
    except Exception as e:
        print(f"An error occured in connection within convert_to_sql: {e}")
    finally:
        connection.close()

#execute SQL query
def execute_query(query):
    connection = sqlite3.connect('historical_data.db')
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()

#run the entire script
def run_script():
    save_to_csv()
    convert_to_sql()

# Main function to execute SQL queries
# def main():
#     query = (
#         "SELECT * "
#         "FROM historical_data "
#         "WHERE Dividends > 0 "
#         "ORDER BY Dividends DESC "
#         "LIMIT 10 ")
#     execute_query(query)

def main():
    query = (
        "SELECT Ticker, MAX(High) AS Highest_Stock_Sale_2023 "
        "FROM historical_data "
        "GROUP BY Ticker")
    execute_query(query)
    query = (
        "SELECT Ticker, Min(Low) AS Lowest_Stock_Sale_2023 "
        "FROM historical_data "
        "GROUP BY Ticker")
    execute_query(query)

if __name__ == "__main__":
    run_script()  # Run the script to pull data and save to CSV and SQL. Data is static, can be removed if already run once. Keep if data is updated at any regular interval
    main()  # Execute SQL query and print to terminal
