"""
Process a text file to count occurrences of the word "Romeo" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

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

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def get_word_count(file_path: pathlib.Path) -> int:
    """Count the number of words in a file."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return len(content.split())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'permalink', a total word count,
     and words per 'permalink' instance, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "all_blogs.txt")
    output_file = pathlib.Path(processed_folder_name, "blog_stats.txt")
    word_to_count: str = "permalink"
    blog_count: int = count_word_occurrences(input_file, word_to_count)
    total_word_count: int = get_word_count(input_file)
    words_per_blog: float = total_word_count / blog_count

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Number of blogs: '{blog_count}'\n")
        file.write(f"Number of words across all blogs: '{total_word_count}'\n")
        file.write(f"Average blog length (number of words): '{words_per_blog:.2f}'\n")
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")
