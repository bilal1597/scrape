# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# req = requests.get(
#     "https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Yjm49OdBzIU")

# soup = BeautifulSoup(req.content, "html.parser")

# weekend = soup.find(id='seven-day-forecast')
# items = weekend.find_all(class_='tombstone-container')

# # print(items[0].find(class_='period-name').get_text())
# # print(items[0].find(class_='short-desc').get_text())
# # print(items[0].find(class_='temp').get_text())

# period_names = [item.find(class_='period-name').get_text() for item in items]
# short_desc = [item.find(class_='short-desc').get_text() for item in items]
# temperature = [item.find(class_='temp').get_text() for item in items]

# # print(period_names)
# # print(short_desc)
# # print(temperature)

# weather = pd.DataFrame(
#     {
#         'periods': period_names,
#         'descriptions': short_desc,
#         'temperatures': temperature,
#     })

# print(weather)

# # weather.to_csv('data.csv')


# # resp = soup
# # print(resp.find_all('title'))
