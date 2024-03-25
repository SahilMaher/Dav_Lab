# 8. Write a single command to show the details (count, min, max,
# mean, std, 25%, 50%, 75%) about the column User Votes.


import pandas as pd


# Read the Excel file
excel_file = 'moives1.xls'
Second_sheet = pd.read_excel(excel_file,sheet_name='2000s')
# Assuming Second_sheet is your DataFrame
# Replace Second_sheet with the name of your DataFrame if it's different
user_votes_details = Second_sheet['User Votes'].describe()




print(user_votes_details)