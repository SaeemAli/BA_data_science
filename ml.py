import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def linearSearch(array, x): # Linear search

    # Going through array sequencially
    for i in range(0, len(array)):
        if (array[i] == x):
            return i
    return -1

""" Retrieve Data """

df = pd.read_csv("data/customer_booking.csv", encoding="ISO-8859-1")

cleanDF = df[['num_passengers', 'sales_channel', 'trip_type', 'length_of_stay', 'flight_hour', 'flight_day',
         'booking_origin', 'flight_duration', 'booking_complete']]

#cleanDF = cleanDF[cleanDF['booking_origin'] != "(not set)"]

channel = cleanDF['sales_channel'].unique()
trip = cleanDF['trip_type'].unique()
country = cleanDF['booking_origin'].unique()
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

channelVal = []
tripVal = []
countryVal = []
day_val = []

for i in range(len(cleanDF)):
    channelVal.append(linearSearch(channel, cleanDF.loc[i, 'sales_channel']))
    tripVal.append(linearSearch(trip, cleanDF.loc[i, 'trip_type']))
    countryVal.append(linearSearch(country, cleanDF.loc[i, 'booking_origin']))
    day_val.append(linearSearch(day, cleanDF.loc[i, 'flight_day']))

cleanDF['sales_channel_value'] = channelVal
cleanDF['trip_value'] = tripVal
cleanDF['country_value'] = countryVal
cleanDF['day'] = day_val

testDF = cleanDF[['num_passengers', 'sales_channel_value', 'trip_value', 'length_of_stay', 'flight_hour', 'day',
         'country_value', 'flight_duration', 'booking_complete']]

""" Training and testing sets """

y = testDF['booking_complete']

x = testDF.drop('booking_complete', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

""" Linear Regression """

# Training the model
lr = LinearRegression()
lr.fit(x_train, y_train)

y_train_lr_pred = lr.predict(x_train)

y_test_lr_pred = lr.predict(x_test)

#print(y_test_lr_pred)

# y_train_lr_pred
# y_test_lr_pred

lr_train_mse = mean_squared_error(y_train, y_train_lr_pred)
lr_train_r2 = r2_score(y_train, y_train_lr_pred)

lr_test_mse = mean_squared_error(y_test, y_test_lr_pred)
lr_test_r2 = r2_score(y_test, y_test_lr_pred)

results = pd.DataFrame(["Linear Regression", lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
results.columns = ["Method", "Training MSE", "Training R2", "Test MSE", "Test R2"]
#print(results)

results.to_csv("data/linearRegression.csv")