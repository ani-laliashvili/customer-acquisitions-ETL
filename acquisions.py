import pandas as pd

# read data
people = pd.read_csv('people.csv')

# get dates from datetime objects
people[['date', 'time']] = people['created_dt'].str.split(' ', 2, expand=True)

# group data by date
dates = people.groupby('date')

# count acquisitions by date
acquisitions_df = dates.count()

# format dataframe
acquisitions_df['date'] = acquisitions_df.index
acquisitions_df = acquisitions_df[['date', 'email']]

# save results
acquisitions_df.to_csv('acquisition_facts.csv', index=False, header=['acquisition_date', 'acquisitions'])
