import pandas as pd

# get data from the data directory
cons_email_chapter_subscription = pd.read_csv('data\\cons_email_chapter_subscription.csv')
cons = pd.read_csv('data\\cons.csv')
cons_email = pd.read_csv('data\\cons_email.csv')

# keep only primary emails
primary_email_df = cons_email[cons_email['is_primary'] == 1]

# choose columns to keep from dataframes
primary_email_df = primary_email_df[['cons_id', 'cons_email_id', 'email', 'create_dt', 'modified_dt']]
cons_email_chapter_subscription = cons_email_chapter_subscription[['cons_email_id', 'chapter_id', 'isunsub']]

# merge primary email and subscription dataframes, keeping all primary email data
people_df = pd.merge(cons_email_chapter_subscription, primary_email_df, on='cons_email_id', how='right')

# if data is missing in subscription dataframe, assume chapter_id = 1 and customer is still subscribed (isunsub=0)
people_df['chapter_id'] = people_df['chapter_id'].fillna(1)
people_df['isunsub'] = people_df['isunsub'].fillna(0)

# keep only chapter_id = 1 values
people_df = people_df[people_df['chapter_id'] == 1]

# merge primary email and consumer dataframes, keeping all primary email data
people_df = pd.merge(cons[['cons_id', 'subsource']], people_df, on='cons_id', how='right')

# format dt values
people_df['create_dt'] = people_df['create_dt'].str.slice(5)
people_df['modified_dt'] = people_df['modified_dt'].str.slice(5)

# choose columns to output
people_df = people_df[['email', 'subsource', 'isunsub', 'create_dt', 'modified_dt']]

# save dataframe
people_df.to_csv('people.csv', index=False, header=['email', 'code', 'is_unsub', 'created_dt', 'updated_dt'])
