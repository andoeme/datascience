import pandas as pd
import numpy as np

# Dictionary as a dataframe (2D table)
# The key is the column, the values are the rows
dataframeData = {
    'column1': np.random.rand(5), # Create 5 random values
    'column2': np.random.rand(5),
    'column3': np.random.rand(5)
    }

#print(dataframeData)

dataframe = pd.DataFrame(dataframeData)
#print("\n", dataframe)

# The dataframe looks like this:
#
#     column1   column2   column3
# 0  0.537531  0.840134  0.142831
# 1  0.935323  0.513498  0.220030
# 2  0.827087  0.917872  0.576367
# 3  0.219176  0.874052  0.484607
# 4  0.669063  0.062128  0.045993




# Open Files

# Open Excel File with pandas and select sheet
# tracksData = pd.read_excel('pandas\\Tracks.xlsx', sheet_name=0)

# Open CSV File with Pandas and make index in first row
flightsData = pd.read_csv('pandas\\flights.csv', index_col=False)

longFlights = flightsData[flightsData['DISTANCE'] >= 4000] # 348 flights
print(longFlights[longFlights['ORIGIN_STATE_NM'] == 'Hawaii']) # 194 flights


# Selecting Data #

# Select column
# data['ORIGIN']

# Select Multiple Columns
# data[['ORIGIN_CITY_NAME', 'DEST_CITY_NAME']]

# Select first 3 rows
# data[:3]

# Locate a specific entry with iloc[rowIndex, columnIndex]
# data.iloc[0,0]

# Use get_loc to get the index of a column
# data.iloc[2, flightsData.columns.get_loc('DAY_OF_MONTH')]

# Select multiple specific entries
# data.iloc[0, [flightsData.columns.get_loc('ORIGIN'), flightsData.columns.get_loc('DEST')]]

# Select multiple rows for specific columns
# data.iloc[:3, [flightsData.columns.get_loc('ORIGIN'), flightsData.columns.get_loc('DEST')]]

#   ORIGIN DEST
# 0    RNO  DEN
# 1    LGA  MCI
# 2    BWI  ISP




# Sorting Data
    # Ascending
        # data.sort_values(by=['DISTANCE'])
    # Descending
        # data.sort_values(by=['DISTANCE'], ascending=False)
    # Sort Multiple Columns
        # flightsData.sort_values(by=['DISTANCE', 'AIR_TIME'])
    



# Filtering Data

# Boolean True/ False
# data['MONTH'] == 1 returns whether January is true or false
# 0          True
# 1          True
# 599970    False
# 599971    False
# [600000 rows x 25 columns]    600.000 total rows

# Select all entries where month equals January
# data[data['MONTH'] == 1]
# [50000 rows x 25 columns]     50.000 flights in January

# Filter with String value
# data[data['ORIGIN_STATE_NM'] == 'New York']
# [25815 rows x 25 columns]     25.815 flights from New York

# Bigger than/ smaller than >, <, <=, >=
# data[data['DISTANCE'] >= 4000])
# [348 rows x 25 columns]   348 flights' distance longer or equal than 5.000

# NOT ~ instead of !




# Group Data

# Store grouped by in variable flightsByMonth
# flightsByMonth = data.groupby('MONTH')

# Select part of the group
# flightsByMonth.get_group(11)      Shows only flights in November (11)

# Get the sum of distance in all months
# flightsByMonth['DISTANCE'].aggregate(np.sum)
# MONTH
# 1     42428340.0
# 2     42392773.0
# 3     42718411.0

# Average of distance flown
# flightsByMonth['DISTANCE'].aggregate(np.mean)

# MAX
# flightsByMonth['DISTANCE'].aggregate(np.max)

# MIN
# flightsByMonth['DISTANCE'].aggregate(np.min)

# Largest distance in all months
# flightsByMonth['DISTANCE'].aggregate(np.sum).max()
# Index of largest value
# flightsByMonth['DISTANCE'].aggregate(np.sum).idxmax())

print("\nEnd...")
