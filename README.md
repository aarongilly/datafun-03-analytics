# datafun-03-analytics

## Overview
This project demonstrates how to fetch and process various types of 
data (Excel, JSON, text, and CSV) using Python. 

The repository includes:

- Four example fetchers: Scripts to retrieve data from the web.
- Four example processors: Scripts to analyze and process the fetched data.

Start by running the examples to understand their functionality, and then build your own scripts to fetch and process data of your choice (using each of these example types).

## DESCRIPTION OF WORK DONE

Below this section is the assignment text. This heading is my submission in response to the assignment text. Each section is grouped by a heading of the file type, which then describes the process and the code therein.

### CSV
For the comma-separated value section of the assignment, I found data.gov, which is an awesome resource for real-world datasets to analyze. In particular I found a dataset for New York State's "Powerball" lottery. I thought it would be funny to run a statistical analysis on the previous 5 years Powerball Numbers to pull out the Mean (average) and Mode (most common) powerball values for each of the 6 balls that are pulled. 

#### CSV Fetcher
The `main()` function calls a helper `fetch_csv_file` function, which uses the `requests` library to make a HTTP request to New York's data repository. The fetch function calls the helper `write_csv_file` function to write the dataset to a directory in accordance with the passed-in variable name (in all cases I used `gillespie_data`).

On my Mac this is run using `python3 gillespie_get_csv.py`

#### CSV Processor
The `main()` function calls a helper `process_csv_file` function, which uses my `analyze_powerball` function to do the heavy lifting. In these two functions the previously saved .csv file is opened, the `Winning Numbers` column (which has a space-separated concatenation of all 6 winning balls) is split into a 2-dimensional list of lists. This 2D list is then split into 6 separate single-dimension lists using 6 separate List Comprehensions. From there, the `statistics` library is used to pull mean and mode. The `process_csv_file` ends by writing up a funny little intro & outro, and the statistics for Powerball, and saving to file.

On my Mac this is run using `python3 gillespie_process_csv.py`

## Excel
For the Excel section of the assignment, I had trouble finding a pre-existing URL that would simply return an Excel document. So I copied a table on [this webpage](https://www.ncaa.com/history/basketball-men/d1) into Excel, then saved the file & pushed it to a separate git repo. This provided a mechanisms to retreive the raw file through a URL. 

The idea with this assignment was to figure out which team has LOST the Men's NCAA National Basketball Champsionship the most, to figure out who has the most disappointed fanbase. I'm sad to say, the alma mater made it into this 4-way tie.

#### Excel Fetcher
The `main()` function calls a helper `fetch_excel_file` function, which uses the `requests` library to make a HTTP request to a git repository I made containing the file. The fetch function calls the helper `write_excel_file` function to write the dataset to a directory in accordance with the passed-in variable name (in all cases I used `gillespie_data`).

On my Mac this is run using `python3 gillespie_get_excel.py`

#### Excel Processor
The `main()` function calls a helper `process_excel_file` function, which uses a `column_to_list` helper function to do convert a single Excel column into a Python list. In these two functions the previously saved .xlsx file is opened, the column `E` (which has a losing team) pulled into a list. This list is analyzed using the `collection` library, which I previously didn't know about and is awesome. This analysis counts the 10 most-losingest-teams, then filters that list to the set that are tied for the greatest number of National Championship *losses*. The `process_excel_file` ends by writing up a funny/depressing little intro & outro, and the statistics for the basketball.

On my Mac this is run using `python3 gillespie_process_excel.py`

## JSON
For the JSON section of the assignment, I was really excited to have the snake eat its own tail. I run (for fun) a Puzzle Box website wherein I make "cyber-physical" puzzles (there's a physical puzzle box and a webpage puzzle and the two interact to make the full puzzle). My Puzzle Box website has an API I am hitting to pull the dataset for the completed playthroughs. I'm hitting that API then calculating the average solve time for each puzzle.

#### JSON Fetcher
The `main()` function calls a helper `fetch_json_file` function, which uses the `requests` library to make a HTTP request to my puzzle box website's API. The fetch function calls the helper `write_json_file` function to write the dataset to a directory in accordance with the passed-in variable name (in all cases I used `gillespie_data`).

On my Mac this is run using `python3 gillespie_get_json.py`

#### JSON Processor
The `main()` function calls a helper `process_json_file` function, which uses a `average_time_to_solve` helper function to load the JSON file to a list of dictonaries, then pull the `duration` key of each dictionary in the list. This key/value pair contains the number of milliseconds each team took between "go" and "final code entered". I am again making use of the `statistics` library to calculate the mean solve time. The `process_excel_file` then calls a formatting `milliseconds_to_duration_string` function (which was sourced from ChatGPT & modified to fit my use case) which converts the integer number of milliseconds into a string containing the associated number of minutes & seconds. Finally, the reuslts are saved into a file named `average_time_for_` followed by the name of the puzzle box being analyzed.

On my Mac this is run using `python3 gillespie_process_json.py`

## Text
For the Text section of the assignment, I continued the theme of using my own content. Similar to the Excel portion of the assignment, I set about making the file I wanted to analyze. I used ChatGPT to jumpstart my coding (outside of this repo) to iterate through a folder full of Markdown Files & combine them into one **large** markdown file containing all my blog entries. This was then uploaded to a public GitHub Gist, which I pulled using its public URL.

I wanted to see the total number of words I've written in my blog over the past decade+, and the average number of words used in a given post.

#### Text Fetcher
The `main()` function calls a helper `fetch_txt_file` function, which uses the `requests` library to make a HTTP request to my public Gist containing all my blog posts, concatenated together in a single file. The fetch function calls the helper `write_txt_file` function to write the dataset to a directory in accordance with the passed-in variable name (in all cases I used `gillespie_data`).

On my Mac this is run using `python3 gillespie_get_text.py`

#### Text Processor
The `main()` function calls a helper `process_text_file` function, which uses a couple of helper functions that each separately load the text file and provide a fact about the file (this could have been optimized by not loading the file twice, but my time is more valuable & premature optimization is to be avoided at all turns). The `count_word_occurences` function gets & return the count of the passed-in word (case-insensitive), in my case I'm counting the word "permalink", which is present in each blog's frontmatter, but unlikely to be used in the body of the blog itself. The `get_word_count` function splits the text by spaces & returns the lenght of the split text. Finally, the results were saved into a file named `blog_stats.txt`.

On my Mac this is run using `python3 gillespie_process_text.py`

---
## Project Workflow

### Step 1. Set Up Your Project
1. Create a GitHub repo with default README.md (you'll need to manually add these example files).
2. Clone your new repo down to your machine. 
3. Open the folder in VS Code.
4. Add a .gitignore file.
5. Install the required packages - see [requirements.txt](requirements.txt).

Full disclosure: We teach building repos from scratch because we assume students want to learn to create their own novel projects. 
However, if you want to get a local copy of this repo down to your machine, you can click the "Use this template" green button to copy it all into your account.  

### Step 2. Run the Examples
If you started with your own repo, copy the files from this GitHub as needed. 
If you cloned the template, you'll have the example files already. 

Read, review, and run each example script. 
Open a terminal in the root project folder and run the appropriate 
command for your operating system. 
For example, these generally work on Windows. 
Adjust the commands to work for your machine, 
e.g. use python3 if Mac/Linux. 

```shell
python3 fetch_scripts/example_get_csv.py
python3 fetch_scripts/example_get_excel.py
python3 fetch_scripts/example_get_json.py
python3 fetch_scripts/example_get_text.py

python3 process_scripts/example_process_csv.py
python3 process_scripts/example_process_excel.py
python3 process_scripts/example_process_json.py
python3 process_scripts/example_process_text.py

```
 
### Step 3. Create and Run Your Data Fetchers
1. Find data files on the web for each type (CSV, Excel, JSON, and text).  
2. Create your own Python script to fetch each type of data and save it in a folder named **data**.
3. Name your scripts:
   1. yourname_get_csv.py
   2. yourname_get_excel.py
   3. yourname_get_json.py
   4. yourname_get_text.py
4. Implement your data-processing logic in small steps:
   - Fetch data for one file type.
   - Test, verify, and Git add-commit-push.
  
## Step 4. Create and Run Your Data Processors
1. Determine a simple metric from each of your data files.  
2. Create your own Python script to read the data, process it, and save it in a folder named **data_processed**.
3. Name your scripts:
   1. yourname_process_csv.py
   2. yourname_process_excel.py
   3. yourname_process_json.py
   4. yourname_process_text.py
4. Work incrementally, using git add-commit-push after each bit of progress. 

## Step 5. Update README.md to Describe Your Work
1. In your README.md, list each of your fetchers with a short description.
2. In your README.md, list each of your processors with a short description of what it does. 
3. Include the execution commands to run your fetchers and processors. 

---

## Helpful Documentation
If you're unsure about any of the setup steps or tools, consult these resources:
- [requests library documentation](https://docs.python-requests.org)
- [GitHub: Create and Clone a Repo](prereqs/01-CreateAndClone.md)
- [Set Up a Virtual Environment](docs/02-SetUpVirtualEnv.md)
- [Create a .gitignore File](docs/03-CreateGitIgnore.md)
- [Using Git: Add-Commit-Push](docs/04-GitAddCommitPush.md)

---

### Tips
- Use descriptive filenames for the data you fetch - and proper file extensions.
- Work incrementally—verify each small step works before moving to the next.
- The examples are required reading - use them to learn and understand first. 
- Test each script carefully before proceeding.
- Use meaningful commit messages when pushing to GitHub to document your progress.

---
## Review Commit History
Once your project is complete, review your commit history in GitHub under the **Commits** tab. 
Ensure your commit messages are clear and professional.

---
## Finalize GitHub

Make sure the following requirements have been met:

- [ ] You have committed a useful .gitignore file.
- [ ] You have committed a useful logs/project_log.log file. 
- [ ] All example scripts executed successfully.
- [ ] Four fetcher scripts created and executed.
- [ ] Four processor scripts created and functional.
- [ ] README.md includes explanations for fetchers and processors with commands for execution.
- [ ] Each Python file contains a docstring with its purpose and input/output details.
