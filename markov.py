"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # feed file_path(arg) to file.read() 
    # return str("contents")

    # print(open(file_path).read())
    # print(type(open(file_path).read()))
    return open(file_path).read()

    # your code goes here

    # return "Contents of your file as one long string"


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # using value of function created above, we're going to split words with .split() with no arguments to break on whitespaces, linebreaks, spaces and tabs
    # convert string to list
    
    word_list = open_and_read_file(input_path).split()
    #print(word_list)
    
    bigram_list = []
    value_list = []

    chains = {}
    
    # loop over list to generate tuples (bigrams)
  
    for i in range(len(word_list) -1):
        # print([word_list[i], word_list[i+1]])
        #new attempt: two loops with two different ranges
        #step 1: get keys
        bigram_tuple = (word_list[i], word_list[i+1])
        bigram_list.append(bigram_tuple)

    for y in range(len(word_list) - 2):
        value_list.extend([word_list[y+2]])

        # create dictionary of keys as tuples
        # find item(word) indexed one more than each bigram
        # create a list of each of these indexed words (not a unique list)
        # assign each list to its key in dictionary
        # introduce condition .get()

    # z = 0
    # for z in range(len(bigram_list)):
    # while z < len(bigram_list):
    # for z in range(len(word_list) - 1):     
    #     # for word_tuple in bigram_list:  
    #     if chains[bigram_list[z]] in chains:
    #         chains[bigram_list[z]] += list(value_list[z])
    #     else:
    #         chains[bigram_list[z]] = list(value_list[z]) 
    #     # z += 1
    # print(bigram_list)
    # print(value_list)

    for word in range(len(bigram_list) -1):
    # for word in bigram_list:
        # print(word)
        # print(chains)
        # chains[word] = chains.get(word, 0) + 1
        if not bigram_list[word] in chains:
            # chains.update({word: list([value_list[z - 1]])})
            chains[bigram_list[word]] = list([value_list[word]])
        else:
            chains[bigram_list[word]].extend([value_list[word]])
            # if chains[word] in chains:
            #     chains[word] = list(value_list[z])
            # else:
            #     chains[word] = list(value_list[z])

    # for word in bigram_list:
    #     chains[word] = chains.get(word, 0) + word

    # goal is to print 
    # print(bigram_list, value_list)
    # print(value_list, type(value_list))
    print(chains)    

    # print(word_list)
#push this to bigram_list

    # convert list of tuples to dictionary keys in our "chains" dictionary
    # values in our chains dictionary will be the words that could follow our keys as lists

    

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
