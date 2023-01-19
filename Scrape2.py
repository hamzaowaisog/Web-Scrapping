from bs4 import BeautifulSoup
import requests

html_url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=PYTHON&txtLocation=').text  #enter url of website
# print(html_url)

soup = BeautifulSoup(html_url , 'lxml')
job = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

for jobs in job :
    publish_date = jobs.find('span', class_='sim-posted').span.text
    if 'few' in publish_date:
        company_name  = jobs.find('h3',class_ ='joblist-comp-name').text.replace(' ','')
        skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = jobs.header.h2.a['href']
        print(f"Company Name : {company_name.strip()}")
        print(f"Required skills : {skills.strip()}")
        print(f"More info : {more_info}")
        print()