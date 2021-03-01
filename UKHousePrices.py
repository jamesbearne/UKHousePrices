# -*- coding: utf-8 -*-
"""

Filename: house_prices.py
Descripton: TBC
TODO#1: Add loop to go through all files in directory
"""
filenames = ["/Users/Phani/Desktop/sales-jan-2015.csv",
"/Users/Phani/Desktop/sales-feb-2015.csv"]
dataframes = []
for f in filenames:
    dataframes.append(pd.read_csv(f))
"""
TODO#2: Change new files to load same columns in order to loop through

"""

import pandas as pd
import os

# Set input data directory
input_dir = r'C:\Users\James.Bearne\Desktop\Python_HousePrice\data\input'

#List the input data files in directory and build filepath
input_files = os.listdir(input_dir)
#TODO#1
input_file = input_files[0] 
input_filepath = os.path.join(input_dir, input_file)

# Read single .csv file into dataframe
df = pd.read_csv(input_filepath, header = None)

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

# Load new files to new dataframe
df_append = pd.read_csv(r'C:\Users\James.Bearne\Desktop\Python_HousePrice\data\pp-2019.csv', header = None)

#TODO#2

# Append two dataframes
df = df.append(df_append, ignore_index=True)

# Remove unintersting columns
df = df[["TRANSFER_DATE", "PRICE", "PROPERTY_TYPE", "POAN", "STREET", "POSTCODE"]]

# Set the postcode and select just those transactions
postcode = 'SW16 2BP'
df_postcode = df.loc[df['POSTCODE'] == postcode]

print(df_postcode.head())