# Day 17 - Web Scraping

# What is Web Scraping?

- The internet is full of huge amount of data which can be used for different purposes
- to collect this data, you have to scrape data from a website
- web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database

# How to Web Scrape

- BeautifulSoup is a python package for web scraping
- Requests is a python package for handling web urls
- to scrape data from websites, basic understanding of HTML tags and CSS selectors is needed
- Content is targeted using html tags, classes or/and ids
- make sure to install the packages using pip before importing them into a file
- declare a url variable for the website which you want to scrape
- the requests get method fetches data from url
- the requests status_code returns 200 if the fetch was successful
- BeautifulSoup is used to parse content from the page

