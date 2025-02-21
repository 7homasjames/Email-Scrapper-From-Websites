import re
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    """Launch Chrome browser and fetch the website content."""
    print("Launching Chrome browser...")

    chrome_driver_path = "./chromedriver.exe"  # Adjust path if needed
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_emails(html_content):
    """Extracts emails from the given HTML content using regex."""
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract visible text
    text_content = soup.get_text(separator=" ")

    # Email regex pattern
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    # Find all unique emails
    emails = set(re.findall(email_pattern, text_content))

    return list(emails)
