# Web-Scraping
Data scarping is a skill that allows you to extract valuable data from websites, process it and store it for future use. It can be used in many efficient ways like price monitoring, study market trend, social media management. The goal of this project is to scrape multiple websites ang get hands on ethical web scraping using python.
# Web Scraped second most top news stories from USNEWS 

Task Description

The tasks involved in this project are as follows:

1.Access the webpage https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390 and extract the list price and current price of a product.

2.Convert the extracted prices to the format "1234.56" (no dollar sign, comma, just a "." separator for cents) using Python's regular expressions (regex) functionality.

3.Print both the list price and the current price to the screen/terminal.

4.Load the webpage https://www.usnews.com/ and extract the URL of the second current top story.

5.Load the webpage obtained in (4), read and print the header as well as the first 3 sentences of the main body to the screen.

Technologies Used

This project uses Python programming language and the following libraries:

requests,
BeautifulSoup


# Instructions
To run the program:

Clone this repository to your local machine.

Install the required libraries using pip install -r requirements.txt.

Run the script web_scraping_example.py.

Output

The program output is the list price and current price of the product extracted from https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390, and the URL, header, and first 3 sentences of the main body of the second current top story extracted from https://www.usnews.com/.


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


# Web Scraped and downloaded first 10 pages of Ebay's search results containing 60 sold "Amazon gift card" per page

Reads all items and parses each item's title, price, and shipping price. Used Regular Expressions on this data to find out what fraction of Amazon gift card sells above the face value.
This project involves web scraping and sport betting. The project is written in a single Python file called project.py. The project is divided into different sections using functions for easy understanding and readability.

There are three files required for this project:

project.py - Contains all the Python code for web scraping and sport betting.

answers.txt - Contains concise answers to the questions asked during web scraping.

screen.txt - Contains the screen output from the web scraping process.

To run the project, the user needs to download all the HTML files from eBay and place them in the same directory as the project.py file.

The project involves two main parts:

Web Scraping - This section involves scraping data from eBay using Python requests and Beautiful Soup. The following tasks were performed during web scraping:

Analyzing the network tab in the browser and answering questions related to the search request, URL variables, and search results.

Writing code to download the first 10 pages of search results and saving them to files named "amazon_gift_card_XX.htm" where XX is the page number.

Parsing the downloaded HTML files using Beautiful Soup and identifying and printing the title, price, and shipping price of each item.

Using Regular Expressions to identify and print to screen gift cards that sold above face value.

Calculating the fraction of Amazon gift cards that sell above face value and discussing the possible reasons behind it.

Sport Betting - This section involves logging into a sports betting website, fctables.com, using Python requests, and verifying the login status. The following tasks were performed during sport betting:

Creating an account on fctables.com and selecting a football game to place a virtual bet.

Analyzing the network tab in the browser and answering questions related to logging in and verifying the login status.

Writing code to log in to the website using Python requests and verifying the login status by checking whether the word "Wolfsburg" appears on the page.
To run the project, the user needs to execute the project.py file. The screen output will be saved to screen.txt. The answers to the questions asked during web scraping will be saved to answers.txt.



