# Toll Rates Scraping Project

This project uses Selenium to extract toll prices from a particular website, which can be useful for analyzing trends in toll prices over time. The scraper script is written in Python and uses the following libraries: BeautifulSoup, Selenium, and pandas.

## Installation

Before running the script, make sure to install the required modules by running the following command:


## Usage

To use the scraper, open the `toll_price_scraper.py` file and modify the `time.sleep()` function on the last line of code. This function sets the time interval between each data extraction. For example, if you want to extract data every 30 minutes, set the time interval to 1800 seconds (60 * 30).

## Output

The scraper outputs a CSV file named `Data_current_date_and_time.csv`. The file contains the following columns:

1. Direction - The direction of travel (e.g. North, South, East, West).
2. Entry - The entry point for the toll road.
3. Exit - The exit point for the toll road.
4. Toll Price - The price of the toll for the specified route.
5. Current Datetime - The date and time at which the data was scraped.

If a route is closed, the scraper may return a "NaN" value for the toll price. This indicates that the route was not operational at the time of scraping.
