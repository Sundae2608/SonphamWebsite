import requests
from bs4 import BeautifulSoup

# Fetch the web page
url = "https://shillerdata.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links with the specified data-aid attribute
links = soup.find_all('a', {'data-aid': 'DOWNLOAD_DOCUMENT_LINK_RENDERED'})

# Loop through the links and find the one with 'ie_data.xls' in the href
file_url = None
for link in links:
    href = link['href']
    if 'ie_data.xls' in href:
        file_url = href
        break

# Complete the URL if it's relative
if file_url and file_url.startswith("//"):
    file_url = "https:" + file_url

if file_url:
    print("File URL:", file_url)

    # Download the file
    file_response = requests.get(file_url)
    with open("ie_data.xls", "wb") as file:
        file.write(file_response.content)

    print("File downloaded successfully!")
else:
    print("File not found.")