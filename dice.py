import requests
import csv
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://www.dice.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', class_='job-listing')

    csv_filename = 'dice_jobs.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Job Title', 'Company', 'Location', 'Description', 'Posted Date'])

        # Loop through each job listing and extract data
        for job in job_listings:
            job_title = job.find('h3', class_='card-title').text.strip()
            company = job.find('span', class_='compName').text.strip()
            location = job.find('span', class_='jobLoc').text.strip()
            description = job.find('div', class_='card-description').text.strip()
            posted_date = job.find('span', class_='posted').text.strip()

            # Write the extracted data to the CSV file
            csv_writer.writerow([job_title, company, location, description, posted_date])

    print(f'Successfully scraped job data and saved to {csv_filename}')
else:
    print('Failed to fetch the webpage.')