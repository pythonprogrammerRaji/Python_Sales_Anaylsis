import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def scrape_jobs(job_role):
    url = f"https://www.freshersworld.com/jobs/jobsearch/{job_role}-jobs"
    
    # Add headers to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Send the request
    response = requests.get(url, headers=headers)
    
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all job listings
    jobs = soup.find_all('div', class_='job-container')

    job_count = 0;
    
    # If no jobs found
    if not jobs:
        print("No jobs found. The website structure may have changed.")
        return 0

    # Loop through jobs and extract info
    for job in jobs:

        # print(job.prettify())
        # break
        # job title
        title_div = job.find('h3') or job.find('a')
        title = title_div.get_text(strip=True) if title_div else 'No Title'


        # Comapnt Name
        # company_div = job.find('span', class_='job')
        # company = company_div.get_text(strip=True) if company_div else 'No Company'

        location_div = job.find('span', class_='job-location')
        location = location_div.get_text(strip=True) if location_div else 'No Location'


        print(f"Title   : {title}")
        # print(f"Company : {company}")
        print(f"Location: {location}")
        print('-' * 40)

        job_count += 1

    return job_count

# Main program
if __name__ == "__main__":
    roles = ['python', 'java', 'data-science', 'react', 'sql']
    job_count = []

    print("\nFetching job data...\n")
    for role in roles:
        print(f"\n Jobs for {role.title()}:")
        count = scrape_jobs(role)
        job_count.append(count)

    plt.figure(figsize=(10, 6))
    plt.bar(roles, job_count, color='skyblue')
    plt.title("Job Availability by Role on FreshersWorld")
    plt.xlabel("Job Role")
    plt.ylabel("Number of Jobs Found")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
