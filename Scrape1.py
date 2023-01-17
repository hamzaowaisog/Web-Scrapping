from bs4 import BeautifulSoup

with open('D:\FAST UNIVERSITY\SEMESTER !\ICT LAB\Assignment 6\html form.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content , 'lxml')

    input_tags = soup.find_all('input')
    print(input_tags)
