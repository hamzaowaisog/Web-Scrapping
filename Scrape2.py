from bs4 import BeautifulSoup
import requests

html_url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=PYTHON&txtLocation=').text  #enter url of website
# print(html_url)

soup = BeautifulSoup(html_url , 'lxml')
jobs = soup.find('li',class_ = 'clearfix job-bx wht-shd-bx')
# print(jobs)
company_name  = jobs.find('h3',class_ ='joblist-comp-name').text.replace(' ','')
print(company_name)