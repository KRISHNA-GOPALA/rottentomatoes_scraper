# Rotten Tomatoes Web Scraper

This Python web scraper fetches the top-rated movies from Rotten Tomatoes and saves them into an Excel file. The scraper extracts movie names, URLs, and introductions from the Rotten Tomatoes "Top 100 Movies" list and saves the data in a structured format for further analysis or reference.

---

## Features
- Scrapes the top-rated movies from Rotten Tomatoes.
- Fetches movie name, URL, and a brief introduction.
- Saves the data into an Excel file (`movies_top100.xls`).
- Easy to set up and run.

---

## Installation

### Prerequisites:
Ensure that you have **Python 3.x** installed. If not, download and install it from [python.org](https://www.python.org/).

### Clone the Repository:
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/rottentomatoes_scraper.git
cd rottentomatoes_scraper
```

## Set Up a Virtual Environment
### Create a virtual environment to keep the project dependencies isolated:
```bash
python -m venv venv
```
### Activate the virtual environment:
Windows:
```bash
venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
### Install Dependencies:
Install the necessary Python libraries using requirements.txt:
```bash
pip install -r requirements.txt
```

## This will install the following dependencies

- requests: A library to handle HTTP requests.
- beautifulsoup4: A library to parse HTML and extract data.
- xlwt: A library for writing Excel files.

## Run the Scraper
To run the scraper, simply execute the Python script:

```bash
python scraper.py
```
## The scraper will

Fetch the top 100 movies from the Rotten Tomatoes Top 100 Movies page.
Scrape the movie name, URL, and introduction for each movie.
Save the data to an Excel file named movies_top100.xls.
The output file will be saved in the same directory as the script.
