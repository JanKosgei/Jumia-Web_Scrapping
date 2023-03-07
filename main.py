#importing necessary libraries
import requests
from bs4 import BeautifulSoup
import csv

#function to get the rating of a product
def get_rating(total_reviews, pos_reviews, neg_reviews):
    if total_reviews == 0:
        return 0
    else:
        return (pos_reviews - neg_reviews)/total_reviews

#specifying the url
URL = 'https://www.jumia.co.ke/'

#sending GET request and parsing the response
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#extracting the deals of the week section
deals_of_the_week = soup.find("div", {"class": "deals-of-the-week"})

#creating CSV file to store results
with open('jumia_ratings.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Brand Name', 'Price (Ksh)', 'Discount (%)', 'Total Number of Reviews', 'Product Rating'])

#function to get the rating of a product
def get_rating(total_reviews, pos_reviews, neg_reviews):
    if total_reviews == 0:
        return 0
    else:
        return (pos_reviews - neg_reviews)/total_reviews

#specifying the url
URL = 'https://www.jumia.co.ke/'

#sending GET request and parsing the response
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#extracting the deals of the week section
deals_of_the_week = soup.find("div", {"class": "deals-of-the-week"})

#creating CSV file to store results
with open('jumia_ratings.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Brand Name', 'Price (Ksh)', 'Discount (%)', 'Total Number of Reviews', 'Product Rating'])























































