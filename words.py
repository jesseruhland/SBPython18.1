def print_upper_words(words):
    """Accepts a list of strings and prints them in capital letters"""
    for word in words:
        print(word.upper())


def print_upper_words_2(words):
    """Accepts a list of strings and prints them in capital letters
    if they begin with 'e' regardless of case"""
    for word in words:
        if word[0] == "e" or word[0] == "E":
            print(word.upper())



def print_upper_words_3(words, must_start_with):
    """Accepts a list of strings and prints them in capital letters
    if they begin with a letter submitted in the second parameter"""
    for word in words:
        for letter in must_start_with:
            word.upper()
            letter.upper()
            if word[0] == letter:
                print(word.upper())