# Email Scraper

## Overview
Email Scraper is a Streamlit-based web application that extracts email addresses from a given website URL. It utilizes Selenium for web scraping and BeautifulSoup for parsing HTML content to identify email addresses.

## Features
- Scrapes a website and extracts email addresses.
- Uses Selenium to render and fetch dynamic content.
- Uses regex to identify email patterns.
- Displays extracted emails in a user-friendly Streamlit interface.

## Installation
### Prerequisites
Ensure you have Python (>= 3.8) installed, along with the required dependencies.

```bash
pip install -r requirements.txt
```

### Clone the Repository
```bash
git clone <repository_url>
cd Email-Scraper
```

## Usage
Run the Streamlit app using:
```bash
streamlit run main.py
```

### Steps to Use
1. Enter the website URL in the input field.
2. Click on **Scrape Emails** to start the extraction process.
3. Extracted emails will be displayed on the screen.

## File Structure
```
Email-Scraper/
│── main.py           # Streamlit UI and application logic
│── scrapper.py       # Web scraping and email extraction logic
│── requirements.txt  # List of dependencies
│── README.md         # Documentation
```

## Dependencies
The application requires the following Python libraries:
```bash
streamlit
selenium
beautifulsoup4
re
```
Additionally, ensure you have **ChromeDriver** installed and update the path in `scrapper.py` accordingly.

## Future Enhancements
- Implement multi-threaded scraping for better performance.
- Support additional data extraction formats.
- Improve email validation to reduce false positives.

## License
This project is licensed under the MIT License.



