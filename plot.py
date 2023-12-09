import re
from collections import Counter

#function to count the number of words in a file
def count_words(file_path):
    word_count = 0
    delimiter = r'\W+'  # Split words using non-alphanumeric characters as delimiter
    dictionary = {}
    with open(file_path, 'r') as file:
        content = file.read()
        words = re.split(delimiter, content)
        word_counts = Counter(words)
        sorted_counts = sorted(word_counts.items(), key=lambda x: x[0])
        return sorted_counts

# Example usage
file_path = 'test.txt'  # Replace with your file path

word_counts = count_words(file_path)
for word, count in word_counts:
    print(f'{word}: {count}')