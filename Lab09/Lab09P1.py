#
# World McCrea
# 6/28/2024
# Word counting in dictionaries
#

# DO NOT UPDATE ANY PART OF THE MAIN FUNCTION
def main():
    input_file = open('word.txt', 'r')  # Open a file for reading
    file_text = input_file.read().upper()  # Read all contents and convert to uppercase
    process_file(file_text)
    input_file.close()

def process_file(text):
    # Create an empty dictionary
    dict1 = {}

    # Use the split method to get a list of words from the input
    words = text.split('\n')
    for line in words:
        line_text = line.strip().split(' ')
        for word in line_text:
            # Increment the count for the word in the dictionary
            dict1[word] = dict1.get(word, 0) + 1  # this is adding a default value. Doesn't throw an error

    # Print the dictionary
    print("Dictionary:", dict1)

    # Create a list of words with the maximum count and print the list
    max_count = max(dict1.values())
    # max_words = []
    # for word, count in dict1.items():
    #     if count == max_count:
    #         max_words.append(word)

    max_words = [word for word, count in dict1.items() if count == max_count]  # comprehension W3Schools
    print(f"Words with max count of {max_count}: {max_words}")

    # Remove the words with max count from the dictionary and print the dictionary
    for word in max_words:
        if word in dict1:
            del dict1[word]
    print("Dictionary after removing max count words:", dict1)

    # Put all the words in the dictionary in a list, sort it, and print the list of sorted words
    sorted_words = sorted(list(dict1.keys()))  # this part was very difficult to figure out. kept giving me errors
    print("Words sorted:", sorted_words)

# Remove this line before submitting to BB.
pass

main()




