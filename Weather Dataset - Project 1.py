import pandas as pd

data = pd.read_csv(r"C:\Users\saqif\Desktop\file.csv")

#read the data
data

#show the first few rows of the dataset, by default first 5
data.head()

#tells us the number of rows and columns present in the dataset
data.shape

#tells us the range index of the data set
data.index

#Provide the information on the columns present in the dataset
data.columns

#Tells us the data types of each column present in the data set
data.dtypes

#Shows unique values, can be only applied to a single column
data['Weather'].unique()

#Shows total of no of unique values in each column
data.nunique()

#shows the total no. of non null values
data.count()

#Shows the count of unique values of a single column
data['Weather'].value_counts()

#Provides basic info
data.info()



#finding the unique wind speed values in the data

data.head(2)
data.nunique()
data['Wind Speed_km/h'].nunique()
data['Wind Speed_km/h'].unique() #Answer

#No. of times when weather is exactly clear

data.head()
data.Weather.value_counts()

#or 

data[data.Weather == 'Clear']

#or 

data.groupby('Weather').get_group('Clear')

#No. of times the wind speed was exactly 4km/hr

data.head(2)
data [data['Wind Speed_km/h'] == 4]

#Null values in the data

data.isnull().sum()

#Rename weather to weather conditions, Inplace true will make the changes permanently

data.rename(columns={'Weather':'Weather Condition'})
data.head(1)

#Mean of Visibility

data.Visibility_km.mean()

#Standard Deviation of Pressure

data.Press_kPa.std()

#Variance of RelativeHumidity

data['Rel Hum_%'].var()

#Count of Snow

data[data.Weather == 'Snow']

#or (for all the values that contain Snow)

data[data.Weather.str.contains('Snow')]


