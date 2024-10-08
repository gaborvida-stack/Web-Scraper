## Web Scraper with Python (OOP-Based)
This is a Python-based web scraping tool that uses `requests` and `bs4` for fetching and parsing HTML content from web pages. The scraper allows the user to search for specific HTML tags, and optionally filter by class, ID, or other attributes. The script has been refactored using OOP principles.

## Features
  - Fetch HTML content from a provided URL
  - Search for specific HTML tags
  - Filter search results by class, ID, or attributes
  - Output text content from the matched HTML elements

## Requirements
  - Python 3 (or higher)
  - `requests`
  - `bs4`

## Installation
  - Clone the repository or download the project files:
    ```
    git clone https://github.com/gaborvida-stack/Web-Scraper.git
    ```
    ```
    cd Web-Scraper
    ```
  - Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Example Usage
  ```bash
  python scraper.py
  ```
  ```python
  Enter URL: https://example.com
  Enter HTML tag to search for: p
  Search by (c)lass, (i)d, or (a)ttributes? (leave empty for none): 
  ```

## Example Output
  ```python
  Response received: code=200
  Found content:
  1. This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.
  2. More information...
  ```
## Code Overview
  - Handles making requests to the URL and obtaining the HTML content.
  - Parses the HTML content using BeautifulSoup and searches for specific tags, classes, IDs, or attributes.
