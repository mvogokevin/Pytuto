import re

# Function to count the number of words in a file
def count_words(file_path):
    # Initialize the word count
    word_count = 0
    delimiters = r'[*,.();#\n\t\r\s\f\v\d]'

    dictionary = {}
    
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read()
            
            # Split the content into words using the specified delimiter
            words = re.split(delimiters, content)

            words = list(filter(None, words))

            for i in words:
                if i in dictionary.keys():
                    continue
                else:
                    count = words.count(i)
                    dictionary.update({i : count})

            results = open("results.txt", "a")

            for key in dictionary:
                results.write(key + "\t=>\t"+ str(dictionary[key])+"\n")


            #print(final)  
            # Count the number of words

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

    return word_count

# File path
file_path = "text.txt"  # Replace with the actual file path

# Count the number of words using default space delimiter
print("Number of words:", count_words(file_path))

# You can also use a specific delimiter, for example, comma
# print("Number of words (using comma delimiter):", count_words(file_path, ","))

