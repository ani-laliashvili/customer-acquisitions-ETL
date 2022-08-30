# ETL

The two scripts accompanying this README file are designed to analyze 
daily customer acquisitions over time. 

The following input files inside a 'data' directory are required for the
process to run:
- cons_email_chapter_subscription.csv 
- cons.csv
- cons_email.csv

Running people.py will produce a people.csv file with primary email 
address, source code, subscription data and time record was created 
and updated.

## Schema for people.csv
Column		          Type		    Description  
email		            string		  Primary email address  
code		            string		  Source code  
is_unsub	          boolean		  Is the primary email address unsubscribed?  
created_dt	        datetime	  Person creation datetime  
updated_dt	        datetime	  Person updated datetime  

Running acquisitions.py will then produce an acquisition_facts.csv file 
with customer acquisition counts for each day. 

## Schema for acquisitions.csv
Column			        Type		  Description
acquisition_date	  date		  Calendar date of acquisition
acquisitions		    int		    Number of constituents acquired on acquisition_date


## Requirements:
- pandas
