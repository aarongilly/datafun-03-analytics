"""
Experimenting with code sourced from ChatGPT, modified slightly. 
Not technically part of the assignment, but fun.

This doesn't return anything or save files anywhere, but does grab
a Pandas DataFrame with the first found table on any given URL. Sweet.
Excited to learn more about pandas soon.
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_wikipedia_table(url):
  """
  Extracts the first table from a given Wikipedia page URL using pandas.

  Args:
    url: The URL of the Wikipedia page.

  Returns:
    A pandas DataFrame containing the extracted table data, or None if no table is found.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = pd.read_html(soup.prettify())
    if tables:
      return tables[2]  # Return the first table found
    else:
      print(f"No tables found on {url}")
      return None
  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    return None

# Example usage:
url = "https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films" # "https://en.wikipedia.org/wiki/List_of_U.S._states" 
df = get_wikipedia_table(url)

if df is not None:
  print(df.head()) 
  