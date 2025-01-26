"""
Process the high scores JSON from my Puzzle Boxes & average them

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json
import statistics

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "gillespie_data"
processed_folder_name: str = "gillespie_processed"
# box_name: str = "Brief Mystery"
# box_name: str = "The Vault"
box_name: str = "Cookie Jar"

#####################################
# Define Functions
#####################################

def average_time_to_solve(file_path: pathlib.Path) -> int:
    """Calculates the average time to solve a puzzle box from the saved JSON file"""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            solve_dictionary = json.load(file)  
            # map dictionary to solve duration list
            solve_durations = [item["duration"] for item in solve_dictionary]
            
            average_time_milliseconds = statistics.mean(solve_durations)
            
            return average_time_milliseconds
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, f"{box_name.replace(' ','_')}.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, f"average_time_for_{box_name.replace(' ','_')}.txt")
    
    average_time_milliseconds = average_time_to_solve(input_file)
    average_time_formatted = milliseconds_to_duration_string(average_time_milliseconds)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write(f"The average solve time for {box_name} is {average_time_formatted}")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")


#####################################
# Helper function for formatting - from ChatGPT, modified for this use case
#####################################
def milliseconds_to_duration_string(milliseconds):
  """
  Converts milliseconds to a string representing minutes and seconds.

  Args:
    milliseconds: The number of milliseconds.

  Returns:
    A string representing the equivalent number of minutes and seconds.
  """
  seconds = milliseconds / 1000
  minutes = seconds // 60
  seconds = seconds % 60 

  return f"{int(minutes)} minutes and {seconds:.2f} seconds" 

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
