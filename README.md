# Web-Scraping
Data scarping is a skill that allows you to extract valuable data from websites, process it and store it for future use. It can be used in many efficient ways like price monitoring, study market trend, social media management. The goal of this project is to scrape multiple websites ang get hands on ethical web scraping using python.
# Web Scraped second most top news stories from USNEWS 

# Barnes & Noble Top 100 Scraper
This repository contains a Python script that scrapes the Barnes & Noble Top 100 Book Bestsellers list and extracts the old price, new price, and book description for each result.

# Requirements
Python 3,
BeautifulSoup4,
Requests.
# Usage

1.Clone this repository to your local machine.

2.Install the required libraries using pip install -r requirements.txt.

3.Run the script using python bn_top100_scraper.py.
The script will save each product page of the top 40 books in “B&N Top 100” to your current working directory with a meaningful filename (e.g., "bn_top100_01.htm"). Each page request is followed by a 5 second pause.

4.After all the pages are downloaded, the script will loop through the downloaded pages, open and parse them into a BeautifulSoup object, and access the “Overview” section of the page to print the first 100 characters of the overview text to the screen.

# Notes
This script is for educational purposes only. Scraping websites without permission may be illegal or against the terms of service of the website.
The code may need to be modified to work with changes to the website's HTML or CSS.
The downloaded product pages can be used for further analysis, such as sentiment analysis or topic modeling.


# Web Scraped and downloaded first 10 pages of Ebay's search results containing 60 sold "Amazon gift card" per page and reads all items and parses each item's title, price, and shipping price. Used Regular Expressions on this data to find out what fraction of Amazon gift card sells above the face value.
