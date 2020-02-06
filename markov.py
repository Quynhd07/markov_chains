"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    # contents = open(sys.argv[1]).read()
    contents = open(file_path).read()
    # contents = contents.replace('\n', ' ')
    # print(contents)
    return contents


def make_chains(text_string, n):
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
    words_list = open_and_read_file(text_string).split()

    chains = {}

    for i in range(0, len(words_list) - n):
        # n_gram = (words_list[i], words_list[i + 1])
        list_gram = []
        for inner_i in range(n):
            list_gram.append(words_list[i + inner_i])

        # convert list of list_gram to tuple
        n_gram = tuple(list_gram)

        value = [words_list[i + n]]

        if n_gram in chains.keys():
            chains[n_gram].extend(value)

        else:
            chains[n_gram] = value

            # TODO: use .get
        # chains += chains.get(chains[current_two_gram], value) +

    # your code goes here

    return chains


def make_text(text_string, n):
    """Return text from chains."""

    # Get all dictionary keys, converts to a list, choose a tuple pair
    # TODO: choice(chains) *does not work
    key = choice(list(make_chains(text_string, n).keys()))
    # converts key to list
    words = list(key)
    print(words)
    # for i in range(n):
    #     words.append(key[i])

    # words = [key[0], key[1]]
    # choose from possible list of values
    value = choice(make_chains(text_string, n)[key])
    print(value)

    # while word exists
    while value:
        words.append(value)

        list_key = []
        for i in range(n-1):
            list_key.append(words_list[i + inner_i])

        key = (set, value)


        # value = choice(chains[key])
        value = choice(make_chains(text_string, n).get(key, [None]))

    return_str = ' '.join(words)
    print(return_str)
    # return ' '.join(words)


    # new_string = ''

    # strt = 0
    # end = 7

    # while end != len(words):
    #     new_string = words[strt:end] + '\n'
    #     print(new_string)
    #     strt += 7
    #     end += 7

    # print(new_string)



    # one_string = ' '.join(words)
    # print(one_string)
    # print(len(one_string))


    # return ' '.join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
