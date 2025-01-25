"""
Process an Excel file to determine the team(s) that most often comes 2nd.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import openpyxl

# Import from local project modules
from utils_logger import logger

from collections import Counter

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "gillespie_data"
processed_folder_name: str = "gillespie_processed"

#####################################
# Define Functions
#####################################

def column_to_list(file_path: pathlib.Path, column_letter: str) -> list:
    """Convert a column of an Excel file stored at the file path to a Python list."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        column_values = []
        for row in sheet.iter_rows(min_col=5, max_col=5, min_row=1, values_only=True):
            value = row[0]
            if value is not None:  # to avoid None values
                column_values.append(value)
        return column_values
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of 'GitHub' in a specific column, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "basketball.xlsx")
    output_file = pathlib.Path(processed_folder_name, "excel_feedback_github_count.txt")
    column_to_check = "E"  # Replace with the appropriate column letter

    runner_ups = column_to_list(input_file, column_to_check)

    # Use Counter to find the most common string
    counter = Counter(runner_ups)
    # most_common_runner_up, count = counter.most_common(1)[0]
    most_common_runners_up= counter.most_common(10)

    # Find the largest count (most frequent occurrence)
    max_count = most_common_runners_up[0][1]  # The count of the most common item
    
    # Filter the teams that have the largest count
    teams_with_max_count = [team for team, count in most_common_runners_up if count == max_count]

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write("The most disappointed NCAA Men's Basketball fanbases of all time belong to:\n")
        for team_name in teams_with_max_count:
            file.write(f"\n- {team_name}")
        file.write(f"\n\n...which lost in {max_count} National Championship games.")
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")
