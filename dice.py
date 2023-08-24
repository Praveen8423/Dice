import csv
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.dice.com'

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract job data
    jobs = []
    # Add your code here to extract job data and append it to the 'jobs' list

    # Store the data in a CSV file
    with open('jobs.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Job Title', 'Description', 'Location', 'Company', 'Vendor', 'Posted Date', 'Job Type', 'Salary/Rate']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
else:
    print('Failed to fetch the webpage.')

