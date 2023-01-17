from bs4 import BeautifulSoup

with open('D:\FAST UNIVERSITY\SEMESTER !\ICT LAB\Assignment 6\html form.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content , 'lxml')
    print(soup.prettify())

    label_tags = soup.find_all('label')
    print(label_tags)

    for label in label_tags:
        print(label.text)


