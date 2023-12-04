import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_and_download(url, download_directory):
    # Make a request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the links to the files within tables
        file_links = []
        for table in soup.find_all('table'):
            for a in table.find_all('a', href=True):
                if '.nc' in a['href']:
                    file_links.append(a['href'])

        # Create a directory to store the downloaded files
        os.makedirs(download_directory, exist_ok=True)

        # Download each file
        for file_link in file_links:
            file_url = urljoin(url, file_link)
            file_name = os.path.join(download_directory, file_link.split("/")[-1])

            # Download the file
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                with open(file_name, 'wb') as f:
                    f.write(file_response.content)
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download: {file_url}")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    
    def process_netcdf(file_path):
        # Open the NetCDF file
        with nc.Dataset(file_path, 'r') as nc_file:
            # Access and print information about variables
            for variable in nc_file.variables:
                print(f"Variable: {variable}")
                print(nc_file[variable][:])  # Print the data for the variable (adjust as needed)

# URL pattern for the pages set to year 2000 January.
base_url = "https://noaa-cdr-precip-cmorph-pds.s3.amazonaws.com/index.html#data/hourly/0.25deg/2000/01/"
download_base_directory = "downloaded_files"

# Iterate over the range of pages
for day in range(1, 32):  # assuming days from 1 to 31
    url = f"{base_url}{day:02d}/"
    download_directory = os.path.join(download_base_directory, f"day_{day:02d}")
    scrape_and_download(url, download_directory)
