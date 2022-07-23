from bs4 import BeautifulSoup
import requests
from csv import writer

URL = "https://clutch.co/"
PAGE = requests.get(URL)
SOUP = BeautifulSoup(PAGE.content, 'html.parser')
links = SOUP.find_all('a', class_ = "sitemap-nav__item")

with open('Company.csv', 'w', encoding = 'utf8', newline = '') as f:
    thewriter = writer(f)
    header = ['Company', 'Website', 'Location','Rating','ReviewCnt','HourlyRate','MinProjectSize','EmployeeSize']
    thewriter.writerow(header)

    for link in links:
        url = URL + link.get('href')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('li', class_ = "provider provider-row sponsor")
        for List in lists:
            Company = List.find('a', class_ = "company_title").text.replace('\n', '')
            Website = List.find('a', class_ = "website-link__item").get('href')
            Location = List.find('span', class_ = "locality").text.replace('\n', '')
            #Contact = List.find('a', class_ = "website-link__item").get('href')
            Rating = List.find('span', class_ = "rating sg-rating__number")
            if(Rating is not None):
                Rating = Rating.text.replace('/n','')
            else:
                Rating = "Nan"
            ReviewCnt = List.find('a', class_ = "reviews-link sg-rating__reviews")
            if(ReviewCnt is not None):
                ReviewCnt = ReviewCnt.text.replace('/n','')
            else:
                ReviewCnt = "Nan"
            HourlyRate = List.find('div', class_ = "list-item custom_popover").text.replace('\n', '')
            MinProjectSize = List.find('div', class_ = "list-item block_tag custom_popover").text.replace('\n', '')
            EmployeeSize = List.find('div', class_ = "list-item block_tag custom_popover").text.replace('\n', '')
            info = [Company, Website, Location, Rating, ReviewCnt , HourlyRate , MinProjectSize , EmployeeSize]
            thewriter.writerow(info)

