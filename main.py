import streamlit as st
from scrapper import scrape_website, extract_emails

# Streamlit UI
st.title("Email Extractor from Websites")

# User input
url = st.text_input("Enter Website URL")

if st.button("Scrape Emails"):
    if url:
        st.write("Scraping the website...")
        
        # Scrape and extract emails
        html_content = scrape_website(url)
        emails = extract_emails(html_content)
        
        if emails:
            st.write("### Extracted Emails:")
            for email in emails:
                st.write(email)
        else:
            st.write("No emails found.")
