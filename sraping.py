import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get(
    "https://ecommerce.thebloodraw.com/")

soup = BeautifulSoup(req.content, "html.parser")

featured = soup.find(
    class_='prd-grid data-to-show-4 data-to-show-lg-3 data-to-show-md-2 data-to-show-sm-2 data-to-show-xs-2 js-category-grid')
items = featured.find_all(
    class_='prd-inside')

# print(items[0])

# print(items[0].find(class_='prd-title').get_text())
# print(items[0].find(class_='price-new').get_text())

title = [item.find(class_='prd-title').get_text() for item in items]
price = [item.find(class_='price-new').get_text() for item in items]

# print(title)
# print(price)


data = pd.DataFrame(
    {
        'titles': title,
        'prices': price,
    })


print(data.to_string())

# data.to_csv('scraping.csv')


# # resp = soup
# # print(resp.find_all('title'))
