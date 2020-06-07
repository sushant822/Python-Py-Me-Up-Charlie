# Let us import the libraries that we'll use for this project
import os
import re

# Inform Python where source text file is stored that will be used for our analysis
txtpath = os.path.join('Resources/paragraph.txt')

# Let us open the text file and read it
# Here we'll use the split function.
# We can store the results of our split operation in temperory variables which we'll use to print the result
with open(txtpath) as text:
    paragraph = text.read()
    sentence_count = re.split("(?<=[.!?]) +", paragraph)
    # Words in English language are seperated by a space, so we can use this logic to split the paragraph into words
    word_count = re.split(' ', paragraph)
    # Since word_count is a list, we can count the number of items in the list by using a for loop
    # Let us create a variable called letter_count and set it to 0
    # for every word in the word_count list, we will increment letter_count by the length of the word
    letter_count = 0
    for word in word_count:
        letter_count = letter_count + len(word)
    
    # Now let us print our results
    print("Paragraph Analysis")
    print("---------------------------")
    print(f"Approximate Word Count: {len(word_count)}")
    print(f"Approximate Sentence Count: {len(sentence_count)}")
    print(f"Average Letter Count: {round((letter_count/len(word_count)), 1)}")
    print(f"Average Sentence Length: {round((len(word_count)/len(sentence_count)), 1)}")
    
# Now we need to output our results to a text file
# We need to specify the file path where our results will be saved
output_file = os.path.join('analysis/paragraph_data.txt')

with open(output_file, 'w',) as txtfile:
    txtfile.write("Paragraph Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Approximate Word Count: {len(word_count)}\n")
    txtfile.write(f"Approximate Sentence Count: {len(sentence_count)}\n")
    txtfile.write(f"Average Letter Count: {round((letter_count/len(word_count)), 1)}\n")
    txtfile.write(f"Average Sentence Length: {round((len(word_count)/len(sentence_count)), 1)}")