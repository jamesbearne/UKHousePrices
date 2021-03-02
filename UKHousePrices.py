# -*- coding: utf-8 -*-
"""

Filename: house_prices.py
Descripton: TBC
TODOs
TODO#2: Update the data in PROPERTY_TYPE + PPD_CATEGORY_STATUS column by joining on reference
TODO#3: Groupby on PROPERTY_TYPE and OLD_NEW as required
TODO#4: Pass in only part of postcode to widen the number of transactions
TODO#5: Handle the PPD_CATEGORY + RECORD_STATUS rows correctly
TODO#6: Plot the price change

"""

import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt

# Set input data directory
input_dir = r'C:\Users\James.Bearne\Desktop\Python_HousePrice\data\input'

# List the input data files in directory and build filepath
list_input_files = os.listdir(input_dir)


# Create empty list to store 
list_dataframes = []

for input_file in list_input_files:    
    input_filepath = os.path.join(input_dir, input_file)    
    list_dataframes.append(pd.read_csv(input_filepath, header = None))
    
    # Debugging: Convert datetime to string format
    now = datetime.datetime.now()
    date_time_now = now.strftime("%m/%d/%Y, %H:%M:%S")     
    print("[COMPLETED " + date_time_now + "]: " + input_filepath)
    
df = pd.concat(list_dataframes)

# Name columns of dataframe
df.columns = ['TRANSACTION_ID',
              'PRICE',
              'TRANSFER_DATE',
              'POSTCODE',
              'PROPERTY_TYPE', # D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
              'OLD_NEW', # Y = a newly built property, N = an established residential building
              'DURATION', #F = Freehold, L= Leasehold
              'POAN',
              'SOAN',
              'STREET',
              'LOCALITY',
              'TOWN',
              'CITY',
              'DISTRICT',
              'PPD_CATEGORY_TYPE', # A = Standard Price Paid entry, B = Additional Price Paid entry
              'RECORD_STATUS' # A = Addition, C = Change, D = Delete
              ]

# Remove unintersting columns
df = df[["TRANSFER_DATE", "PRICE", "PROPERTY_TYPE", "POAN", "STREET", "POSTCODE", "RECORD_STATUS"]]

# Set the postcode and select just those transactions into dataframe
#TODO#4
postcode = 'SW16 2BP'
df_postcode = df.loc[df['POSTCODE'] == postcode]
df_postcode = df_postcode.sort_values(by="TRANSFER_DATE", ascending = False)

# Update the data type of TRANSFER_DATE to datetime
df_postcode["TRANSFER_DATE"] = pd.to_datetime(df_postcode["TRANSFER_DATE"])

#Add a new "TRANSFER_YEAR column to the dataframe
df_postcode["TRANSFER_YEAR"] = df_postcode["TRANSFER_DATE"].dt.year

#TODO#5

# Set output data directory and filename
output_dir = r'C:\Users\James.Bearne\Desktop\Python_HousePrice\data\output'
output_file = 'output_postcode.csv'
output_filepath = os.path.join(output_dir, output_file)

# Save the selected transfers to csv file
df_postcode.to_csv(path_or_buf = output_filepath, header = True, index = False)

# Group by certain columns to get yearly mean average
#TODO#3
df_postcode_groupby = df_postcode.groupby(["TRANSFER_YEAR"]).mean()

print(df_postcode_groupby)

# Plot the price change
df_postcode_groupby.plot.bar()












