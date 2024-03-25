'''5. Write a program to create a data frame to maintain three
students’ names associated with their grades in three courses and
then add a new column named Mean to maintain the calculated
mean mark per course. Display the final data frame.'''
import pandas as pd

# Create a dictionary with student names and their grades
data = {
    'Student': ['Bhagat', 'Ram', 'Shita'],
    'Java': [85, 90, 88],
    'DAV': [80, 92, 85],
    'Python': [78, 85, 90]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Calculate mean for each course and add a new column 'Mean'
df['Mean'] = df[['Java', 'DAV', 'Python']].mean(axis=1)

# Display the final DataFrame
print("Final Data Frame:")
print(df)

    main()
