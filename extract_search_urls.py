import re
from bs4 import BeautifulSoup

# Function to extract and filter URLs from an HTML file
def extract_and_filter_urls_from_html(file_path):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Define the regex pattern to match the desired URL structure
    pattern = re.compile(r'^https://google\.com/search\?q=')

    # Find all anchor tags and extract the href attribute if it matches the pattern
    filtered_urls = []
    for a_tag in soup.find_all('a', href=True):
        url = a_tag['href']
        if pattern.match(url):
            filtered_urls.append(url)

    return filtered_urls

# Example usage
file_path = 'C:\\Users\\lefeh\\Downloads\\takeout-20240611T052421Z-001\\Takeout\\My Activity\\Search\\MyActivity.html'
filtered_urls = extract_and_filter_urls_from_html(file_path)
for url in filtered_urls:
    print(url)
