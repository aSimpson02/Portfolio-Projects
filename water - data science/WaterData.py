# Importing relevant libraries:
import pandas as pd

# Using pandas to read, clean, and sort (and convert) the first csv (water quality data):
dataA = pd.read_csv('water_data2.csv')
dataA = dataA.sort_values(by='rank', ascending=True)
print(dataA.index)

# SlicedData is commented out, so I'm assuming it's not needed.
# slicedData = data.iloc[0:4, 0:5]

data1 = dataA[['country', 'rank', 'score', 'landAreaKm']]
data1.to_csv('cleaned_water_data.csv', index=False)

# Using pandas to read, clean, and sort (and convert) the second csv (coordinates of each country):
dataB = pd.read_csv('world_country_and_usa_states_latitude_and_longitude_values.csv')
# Sorting dataB by 'country' column
dataB = dataB.sort_values(by='country', ascending=True)
print(dataB.index)

data2 = dataB[['latitude', 'longitude', 'country']]
data2.to_csv('cleaned_country_data.csv', index=False)

# Merging the two data sets together:
data = pd.merge(data1, data2, on='country')
data.info()
data.to_csv('cleaned_data.csv', index=False)

# Using pandas to read, clean, and sort (and convert) the final CSV (including GDP data):
dataC = pd.read_csv('gdp_per_country.csv')
data3 = dataC[['Country Name', '2020 [YR2020]', '2013 [YR2013]']]
df = data3.rename(columns={'Country Name': 'country'})

dataD = pd.read_csv('world_country_and_usa_states_latitude_and_longitude_values2.csv')
data4 = dataD[['latitude', 'longitude', 'country']]

# Merging the data sets together:
Finaldata = pd.merge(data, df, on='country').merge(data4, on='country')
Finaldata.to_csv('data.csv', index=False)
print(Finaldata.index)
