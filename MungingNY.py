############################################################################################
# Data Munging for Tableau
# Gary Schulke
# February 02, 2020
############################################################################################
############################################################################################
############################################################################################

############################################################################################
# Section 1
#
############################################################################################

import pandas as pd
import glob
import os
# Finish cleaning with Pandas
# Comment / uncomment out file and periodTags as need.
# The path to our CSV file

source_folder = ''


files = [f for f in glob.glob(
    source_folder + "**/*-citibike-tripdata.csv", recursive=True)]
print(files)
for file in files:
    print(file)
    # Read data into pandas
    df = pd.read_csv(source_folder + file)

    # Rename the columns
    headings = {'tripduration': 'tripduration', 'starttime': 'starttime', 'stoptime': 'stoptime',
                'start station id': 'start_station_id', 'start station name': 'start_station_name',
                'start station latitude': 'start_station_latitude',
                'start station longitude': 'start_station_longitude',
                'end station id': 'end_station_id', 'end station name': 'end_station_name',
                'end station latitude': 'end_station_latitude',
                'end station longitude': 'end_station_longitude',
                'bikeid': 'bikeid', 'usertype': 'usertype', 'birth year': 'birth_year',
                'gender': 'gender'}
    df = df.rename(columns=headings)
    df.index.name = 'index'
    df4060 = df[df['birth_year'].isin([1950, 1960, 1970, 1980])]
    df4060['year'] = pd.to_datetime(df4060['starttime']).dt.year
    print(f'Creating: {file}4070.csv')
    df4060.to_csv(source_folder + file + '4070.csv')
