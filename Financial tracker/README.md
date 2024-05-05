# Financial Data Tracker

This project is a Python script designed to pull financial data from Yahoo Finance using the `yfinance` library, store it in both CSV and SQLite formats, and execute SQL queries against the data. It allows users to analyze historical stock prices for selected companies during a specified timeframe.

## Table of Contents

- Installation
- Usage
- Dependencies
- License

## Installation

To use this script, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `https://github.com/MyGollyGosh/Python-Portfolio/tree/main/Financial%20tracker`.
   
2. **Install Dependencies**: Ensure you have Python installed on your machine. Install the required dependencies using `pip install -r requirements.txt`.

3. **Run the Script**: Execute the `main.py` script using `python main.py`. This will pull financial data, save it to CSV and SQLite formats, and execute predefined SQL queries.

## Usage

### Customization

You can customize the script by modifying the following parameters in the `main.py` file:

- `company_tickers`: List of stock ticker symbols for the companies you want to track.
- `start_date` and `end_date`: Define the timeframe for which you want to pull historical data.

### Running Queries

The `main()` function in `main.py` file contains predefined SQL queries. You can modify these queries or add your own to analyze the data according to your requirements.

## Dependencies

This project relies on the following Python libraries:

- `yfinance`: For pulling financial data from Yahoo Finance.
- `pandas`: For data manipulation and analysis.
- `sqlite3`: For working with SQLite databases.

You can install these dependencies using `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
