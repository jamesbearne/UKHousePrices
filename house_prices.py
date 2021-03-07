# -*- coding: utf-8 -*-
"""

@filename: house_prices.py
@created on:
@TODOs
TODO#2: Update the data in PROPERTY_TYPE + PPD_CATEGORY_STATUS column by joining on reference
TODO#3: Groupby on PROPERTY_TYPE and OLD_NEW as required
TODO#5: Handle the PPD_CATEGORY + RECORD_STATUS rows correctly
TODO#6: Plot the price change... DataFrame.Value.Diff()
df['over_the_month'] = df.Value.diff()
df['over_the_year'] = df.Value.diff(12
TODO#7: Add some GUI for input
import tkinter as tk

"""

import pandas as pd
import os
import datetime

# Add reference data as dictionary and then load to dataframe
dict_ref_property_type = {
    "PROPERTY_TYPE": ["D", "S", "T", "F", "O"],
    "DESCRIPTION": ["Detached", "Semi-Detached", "Terraced", "Flats/Maisonettes", "Other"]
    }

df_ref_property_type = pd.DataFrame(data = dict_ref_property_type)

dict_ref_old_new = {
    "OLD_NEW": ["Y", "N"],
    "DESCRIPTION": ["a newly built property", "an established residential building"]
    }

df_ref_old_new = pd.DataFrame(data = dict_ref_old_new)

dict_ref_duration = {
    "DURATION": ["F", "L"],
    "DESCRIPTION": ["Freehold", "Leasehold"]
    }

df_ref_duration = pd.DataFrame(data = dict_ref_duration)

dict_ref_ppd_category_type = {
    "PPD_CATEGORY_TYPE": ["A", "B"],
    "DESCRIPTION": ["Standard Price Paid entry", "Additional Price Paid entry"]
    }

df_ref_ppd_category_type = pd.DataFrame(data = dict_ref_ppd_category_type)

dict_ref_record_status = {
    "RECORD_STATUS": ["A", "C", "D"],
    "DESCRIPTION": ["Addition", "Change", "Delete"]
    }

df_ref_record_status = pd.DataFrame(data = dict_ref_record_status)

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
              'PROPERTY_TYPE',
              'OLD_NEW',
              'DURATION',
              'POAN',
              'SOAN',
              'STREET',
              'LOCALITY',
              'TOWN',
              'CITY',
              'DISTRICT',
              'PPD_CATEGORY_TYPE',
              'RECORD_STATUS'
              ]

# Remove unintersting columns
df = df[["TRANSFER_DATE", "PRICE", "PROPERTY_TYPE", "POAN", "STREET", "POSTCODE", "RECORD_STATUS"]]

# Set the postcode and select just those transactions into dataframe
postcode = input("Enter postcode: ")
df_postcode = df[df['POSTCODE'].str.contains(postcode, regex = False, na = False)]
df_postcode = df_postcode.sort_values(by="TRANSFER_DATE", ascending = False)

# Update the data type of TRANSFER_DATE to datetime
df_postcode["TRANSFER_DATE"] = pd.to_datetime(df_postcode["TRANSFER_DATE"])

#Add a new "TRANSFER_YEAR column to the dataframe
df_postcode["TRANSFER_YEAR"] = df_postcode["TRANSFER_DATE"].dt.year
df_postcode["TRANSFER_MONTH"] = df_postcode["TRANSFER_DATE"].dt.month

# Merge with PROPERTY_TYPE reference data
df_postcode.merge(df_ref_property_type, left_on = 'PROPERTY_TYPE', right_on = 'PROPERTY_TYPE')

#TODO#5

# Set output data directory and filename
output_dir = r'C:\Users\James.Bearne\Desktop\Python_HousePrice\data\output'
output_file = 'output_postcode_' + postcode + '.csv'
output_filepath = os.path.join(output_dir, output_file)

# Save the selected transfers to csv file
df_postcode.to_csv(path_or_buf = output_filepath, header = True, index = False)

# Group by certain columns to get yearly mean average
#TODO#3
df_postcode_groupby = df_postcode.groupby(["TRANSFER_YEAR", "TRANSFER_MONTH"]).mean()

# Plot the price change
df_postcode_groupby.plot.bar()

print(df_postcode_groupby)












