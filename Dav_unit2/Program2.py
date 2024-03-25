'''2. Write a program to read text file data and create a dictionary of
all keywords in the text file. The program should count how many
times each word is repeated inside the text file and then find the
keyword with a highest repeated number.The program should
display both the keywords dictionary and the most repeated word.'''
import re

def count_keywords(file_path):
    keyword_count = {}
    most_repeated_word = ''
    highest_count = 0

    with open(file_path, 'r') as file:
        text = file.read().lower()  # Read the file and convert text to lowercase

    # Use regular expression to find words in the text
    words = re.findall(r'\b\w+\b', text)

    # Count occurrences of each word
    for word in words:
        if word in keyword_count:
            keyword_count[word] += 1
        else:
            keyword_count[word] = 1

        # Update most repeated word and its count if necessary
        if keyword_count[word] > highest_count:
            most_repeated_word = word
            highest_count = keyword_count[word]

    return keyword_count, most_repeated_word

def main():
    file_path = input("Enter the path to the text file: ")
    keywords, most_repeated_word = count_keywords(file_path)

    print("Keywords dictionary:")
    for word, count in keywords.items():
        print(f"{word}: {count}")

    print(f"\nThe most repeated word is '{most_repeated_word}' with {keywords[most_repeated_word]} occurrences.")

if __name__ == "__main__":
    main()

