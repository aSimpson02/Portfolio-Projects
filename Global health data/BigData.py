#importing relevant libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


#web scraping current population data, to show ratio of people in affected areas:
url = "https://www.worldometers.info/world-population/population-by-country/"
result = requests.get(url)

soup = BeautifulSoup(result.text,'lxml')

table = soup.find('table', {'id': 'example2'})#.find_all('tr')
rows = table.find_all('tr') 

country_data = []


for row in rows[1:]:
    row_data = []
    for td in row:
        if td.text.strip() != "":
            row_data.append(td.text.strip())
        #row_data.append(td.text)
    country_data.append(row_data)



#using pandas on dataset:
df = pd.DataFrame(country_data)
df.to_csv('Country_Data.csv', index = False)
df = df.rename(columns={ 1 : 'country', 2: 'population', 5 :'density', 3 :'yearly change'})
df = df[['country', 'population', 'density', 'yearly change']]



#adding in coordinates of each country from a imported CSV file, for mapbox:
dataA = pd.read_csv('world_country_coordinates.csv')
print(dataA.index)
dataA = dataA[['latitude', 'longitude', 'country']]




#*************

#adding a CSV on the amount of global health records produced from each country:
dataB = pd.read_csv('Global_health_data.csv')
print(dataB.index)
dataB = dataB.rename(columns={'location_name' : 'country',})

#cleaning out any years that ismt 1990 and 2019
is_2019 = (dataB['year_id'] == '2019')
is_1990 = (dataB['year_id'] == '1990')
#year = is_2019 - is_1990

#finding the total val
#tot_val = (dataB['val'] == '2019')
i = dataB[dataB['indicator_name'] == 'Breast cancer']

#filtering out the rows
dataB = dataB[['country',i, is_1990, is_2019]]

#merging the all data sets together:
data = pd.merge(dataA, dataB, on='country').merge(df, on ='country')

#turning data into a csv 
data.info()
data.to_csv('cleaned_BigData.csv', index=False)