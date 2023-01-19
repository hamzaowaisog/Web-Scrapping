import time

from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with ")
unfamiliar_skill = input('>')
print(f"Filterting out : {unfamiliar_skill}")
def find_job():
    html_url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=PYTHON&txtLocation=').text  #enter url of website
    # print(html_url)

    soup = BeautifulSoup(html_url , 'lxml')
    job = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index, jobs in enumerate(job) :
        publish_date = jobs.find('span', class_='sim-posted').span.text
        if 'few' in publish_date:
            company_name  = jobs.find('h3',class_ ='joblist-comp-name').text.replace(' ','')
            skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = jobs.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'push/{index}.txt','w') as f:
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f"Required skills : {skills.strip()}\n")
                    f.write(f"More info : {more_info}\n")
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minutes......")
        time.sleep(time_wait *60)