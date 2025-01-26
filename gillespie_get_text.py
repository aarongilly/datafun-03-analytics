"""
This file fetches a text file from the web 
and saves it to a local file named all_columns.txt in a folder named gillespie_data.

Please save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "gillespie_data"

#####################################
# Define Functions
#####################################

def fetch_txt_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch text data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the text file to fetch.

    Returns:
        None

    Example:
        fetch_txt_file("data", "romeo.txt", "https://example.com/romeo.txt")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching text data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: Text file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_txt_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write text data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): Text content to write to the file.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: Data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing to file {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to fetch text data.
    """
    txt_url = 'https://gist.githubusercontent.com/aarongilly/55ca14866a40b93e422163b5b3452183/raw/bafb1f2f4bfc77f663e50bafd5382db44b342cc6/combined.md'
    logger.info("Starting text fetch...")
    fetch_txt_file(fetched_folder_name, "all_blogs.txt", txt_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
