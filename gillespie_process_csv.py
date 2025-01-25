"""
Process a CSV file on Powerball numbers since 2020 in New York, finding the most common winning numbers.

Powerball note: 
A player may select five different numbers, from 1 through 69 and one additional number from 1 through 26.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "gillespie_data"
processed_folder_name: str = "gillespie_processed"

#####################################
# Define Functions
#####################################

def analyze_powerball(file_path: pathlib.Path) -> dict:
    """Analyze the Powerball results column to calculate mode of each result."""
    try:
        # initialize an empty list to store the scores
        winning_numbers_list_of_lists = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    winning_number_list = row["Winning Numbers"].split()  # Extract to list
                    # convert to 
                    winning_numbers_list_of_lists.append(winning_number_list)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")

        # Convert 2d List of strings to 6 one-dimensional list of integers
        ball_one = [int(ball[0]) for ball in winning_numbers_list_of_lists]
        ball_two = [int(ball[1]) for ball in winning_numbers_list_of_lists]
        ball_three = [int(ball[2]) for ball in winning_numbers_list_of_lists]
        ball_four = [int(ball[3]) for ball in winning_numbers_list_of_lists]
        ball_five = [int(ball[4]) for ball in winning_numbers_list_of_lists]
        ball_six = [int(ball[5]) for ball in winning_numbers_list_of_lists]

        # Calculate statistics
        stats = {
            "1_mean": statistics.mean(ball_one),
            "1_mode": statistics.mode(ball_one),
            "2_mean": statistics.mean(ball_two),
            "2_mode": statistics.mode(ball_two),
            "3_mean": statistics.mean(ball_three),
            "3_mode": statistics.mode(ball_three),
            "4_mean": statistics.mean(ball_four),
            "4_mode": statistics.mode(ball_four),
            "5_mean": statistics.mean(ball_five),
            "5_mode": statistics.mode(ball_five),
            "6_mean": statistics.mean(ball_six),
            "6_mode": statistics.mode(ball_six)
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Powerball results, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "powerball_numbers.csv")
    output_file = pathlib.Path(processed_folder_name, "powerball_stats.txt")
    
    stats = analyze_powerball(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Powerball Statistics - aka 'Gauranteed Retirement Plan'\n\n")
        file.write("Regular Balls:\n")
        file.write(f"1: mean = {stats['1_mean']:.2f} & mode = {stats['1_mode']}\n")
        file.write(f"2: mean = {stats['2_mean']:.2f} & mode = {stats['2_mode']}\n")
        file.write(f"3: mean = {stats['3_mean']:.2f} & mode = {stats['3_mode']}\n")
        file.write(f"4: mean = {stats['4_mean']:.2f} & mode = {stats['4_mode']}\n")
        file.write(f"5: mean = {stats['5_mean']:.2f} & mode = {stats['5_mode']}\n\n")
        file.write("The Powerball\n")
        file.write(f"6: mean = {stats['6_mean']:.2f} & mode = {stats['6_mode']}\n\n")
        file.write("Good luck.\n\nMay the odds be ever in your favor.")

    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
