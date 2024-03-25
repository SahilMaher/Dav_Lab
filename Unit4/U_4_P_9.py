
'''9. Extract first and last column in one table.'''

import pandas as pd

# Define the tabular data dictionary
data = {
    'Animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'Age': [2.5, 3.5, 0.5, 0, 5.0, 2.0, 4.5, 0, 7.0,3.0],
    'Priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no',' no'],
    'Visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

    
}

# Define the index labels
index_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(data, index=index_labels)
# Extracting the first and last columns
first_last_columns = df.iloc[:, [0, -1]]

# Display the extracted columns
print(first_last_columns)
