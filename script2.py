import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/corporate-initiatives/levels/supplementary-immigration-levels-2026-2028.html"

# Fetch the webpage content
response = requests.get(url)
response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table directly by its ID
target_table = soup.find('table', id='pr')

if target_table:
    # Convert the BeautifulSoup table object to a string for pandas.read_html
    table_html_string = str(target_table)

    # Use pandas to read the HTML table into a list of DataFrames
    # Even if there's only one table, read_html returns a list
    tables = pd.read_html(table_html_string)

    df_targets = tables[0]