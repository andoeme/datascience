import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt # Needed to show plot in window
from scipy.stats import linregress # Linear Regression Model

# Open CSV File flights.csv
flights = pd.read_csv('pandas\\flights.csv', index_col=False)



# DATA CLEANING

# Convert Columns to correct data types
# flights.dtypes    Shows types of entries in columns

# Convert Date from String to Datetime Format
#flights['FL_DATE'] = pd.to_datetime(flights['FL_DATE'])

# Change Cancelled and Diverted from float64 to boolean
#flights['CANCELLED'] = flights['CANCELLED'].astype(np.bool)
#flights['DIVERTED'] = flights['DIVERTED'].astype(np.bool)

# Delete unneeded columns and modify dataframe immediately
# Without separately storing it like flights = flights.drop...
#flights.drop(columns=['YEAR', 'MONTH', 'DAY_OF_MONTH'], inplace=True)

# Rename columns
#flights.rename(columns={'DEST': 'DESTINATION'}, inplace=True)

# Get amount of null values per column
#flights.isnull().sum()

# Remove null values from dataset
#flights['AIR_TIME'] # 600.000 entries
#flights['AIR_TIME'].dropna() # 590.134 entries after removing missing/null/NaN values



# PLOTTING

# Make histogram from data
#flights['CRS_DEP_TIME'].hist()
# Open new window to display the histogram
#plt.show() 

#flights['CRS_ARR_TIME'].hist()
#plt.show()

# Show average distance by month
flightsByMonth = flights.groupby('MONTH')
#flightsByMonth['DISTANCE'].aggregate(np.mean).plot()
#plt.show()

# Show average distance by day of the week
flightsByDayOfWeek = flights.groupby('DAY_OF_WEEK')
#flightsByDayOfWeek['DISTANCE'].aggregate(np.mean).plot()
#plt.show()



# JOINING DATA

# Merge DAY_OF_WEEK with Description (string of weekday like 'Monday')
dayOfWeek = pd.read_csv('pandas\\L_WEEKDAYS.csv', index_col=False)
merged = pd.merge(flights, dayOfWeek, left_on='DAY_OF_WEEK', right_on='Code')

# Remove reduntant columns 'DAY_OF_WEEK' and 'Code'
merged.drop(columns=['DAY_OF_WEEK', 'Code'], inplace=True)

# Rename 'Description' to 'DAY_OF_WEEK'
merged.rename(columns={' Description': 'DAY_OF_WEEK'}, inplace=True)



# BASIC STATISTICS

# dataframe.describe()
# Displays for every column:
    # count, mean, std, min, max, 25%, 50%, 75%
    # std = Standard deviation. Lower means less deviation, higher more
    # 25%, ... are called 'quartiles'
    # 50% is the 'median' or 'middle value'
print(merged.describe())



# LINEAR REGRESSION

# Get a sample of 1.000 entries from the 600.000 entries
flightsSubsample = flights.sample(1000)
print(flightsSubsample.describe())

# Calculate Linear Regression
# Store results in variables
slope, intercept, r, p, std = linregress(flightsSubsample['DISTANCE'], flightsSubsample['CRS_ELAPSED_TIME'])
print('y = {}*x + {}; r = {}'.format(slope, intercept, r))

# Calculate x and y coordinates to display Linear Regression line
x = np.linspace(flightsSubsample['DISTANCE'].min(), flightsSubsample['DISTANCE'].max(), 1000)
y = slope * x + intercept

# Plot the scatter chart with x and y coordinates
plt.scatter(flightsSubsample['DISTANCE'], flightsSubsample['CRS_ELAPSED_TIME'])

# Plot the Linear Regression Line
plt.plot(x, y, 'r--')

# Display the diagram with both data and linear regression line
plt.show()

# Predict the time needed for a specific distance based on the sample data
distance = 5000
flightTime = slope * distance + intercept
print('{} minutes'.format(flightTime))