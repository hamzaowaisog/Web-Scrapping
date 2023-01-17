from bs4 import BeautifulSoup
import requests

html_url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=PYTHON&txtLocation=').text  #enter url of website
# print(html_url)

soup = BeautifulSoup(html_url , 'lxml')
