# Repository Name: Kalanjiyam Scraper

## Overview
The Kalanjiyam Scraper is a web scraping tool that is designed to scrape content from the website "https://store.tamillexicon.com/". It is specifically designed to scrape Tamil language verses from various authors available on the website and save them in text files for further use.

## Folder Structure
The repository contains the following folder structure:

```
kalanjiyam-scraper/
│
├── scraper_service.py
├── scraper_utils.py
└── kalanjiyam/
└── author1/
│ ├── content_header1.txt
│ └── content_header2.txt
│
└── author2/
└── content_header1.txt
```


The `kalanjiyam-scraper` folder is the root folder of the repository, and it contains two Python files: `scraper_service.py` and `scraper_utils.py`. The `kalanjiyam` folder is the directory where the scraped content is saved in text files, organized by author.

## Files

### 1. `scraper_service.py`
This is the main Python script that implements the web scraping functionality. It contains the following classes and methods:

- `Kalanjiyam` class: Represents the main web scraper class.
  - `__init__()`: Constructor method that initializes the object with the home URL of the website and an empty dictionary to store content links.
  - `get_list_of_authors()`: Method that scrapes the list of authors from the home page and returns a dictionary containing the author names as keys and their corresponding links as values.
  - `get_contents_of_author(author_link)`: Method that scrapes the content headers and their links for a specific author and returns a dictionary containing the content headers as keys and their links as values.
  - `parse_ul(section_tag)`: Recursive method that parses the nested unordered list (ul) tags in the HTML and extracts the content links from them.
  - `scrape_content_verses(author, header, link)`: Method that scrapes the verses from a specific content header link and saves them in a text file, organized by author and content header.
  - `scrape_kalanjiyam()`: Method that orchestrates the entire scraping process, by calling the above methods in a sequence to scrape content from all authors.

### 2. `scraper_utils.py`
This is a utility module that contains helper functions used by the web scraper in `scraper_service.py`. It includes the following functions:

- `make_a_soup(url:str, verify=False)`: Function that takes a URL as input and makes an HTTP GET request to that URL using the `requests` library. It includes a custom User-Agent header to mimic a web browser. The response is then parsed as HTML using BeautifulSoup and the resulting `soup` object is returned. The `verify` parameter is used to specify whether SSL certificate verification should be performed during the request, and it is set to `False` by default.

- `headers`: Dictionary that contains the User-Agent header to be used in the HTTP requests. It specifies the user agent string to mimic a web browser (Mozilla Firefox in this case).

## Usage
To use the Kalanjiyam Scraper, follow these steps:

1. Install the required Python libraries: BeautifulSoup and requests.
2. Ensure that the `scraper_service.py` and `scraper_utils.py` files are present in the same directory.
3. Run the `scraper_service.py` script using a Python interpreter to start scraping content from the website
