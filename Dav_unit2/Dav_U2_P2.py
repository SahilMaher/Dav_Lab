# import re

# def count_keywords(file_path):
#     keyword_count = {}
#     most_repeated_word = ''
#     highest_count = 0

#     with open(file_path, 'r') as file:
#         text = file.read().lower()  # Read the file and convert text to lowercase

#     # Use regular expression to find words in the text
#     words = re.findall(r'\b\w+\b', text)

#     # Count occurrences of each word
#     for word in words:
#         if word in keyword_count:
#             keyword_count[word] += 1
#         else:
#             keyword_count[word] = 1

#         # Update most repeated word and its count if necessary
#         if keyword_count[word] > highest_count:
#             most_repeated_word = word
#             highest_count = keyword_count[word]

#     return keyword_count, most_repeated_word

# def main():
#     file_path = input("Enter the path to the text file: ")
#     keywords, most_repeated_word = count_keywords(file_path)

#     print("Keywords dictionary:")
#     for word, count in keywords.items():
#         print(f"{word}: {count}")
#         dic={}
#         dic[f"{word}"]=f"{count}"
   

#     print(f"\nThe most repeated word is '{most_repeated_word}' with {keywords[most_repeated_word]} occurrences.")

# if __name__ == "__main__":
#     main()
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
