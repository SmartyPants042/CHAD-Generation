f = open('./Classification/Helpers/CMU_dict')
words_string = f.readlines()

def get_phones(given_word):
    """
    Uses Binary Search to get the phonetic composition
    of the given word.

    returns the composition, along with the word itself.
    """
    low = 0
    high = len(words_string)-1

    while low <= high:
        mid = (low+high)//2

        word = words_string[mid].split()[0].lower()

        if word < given_word:
            low = mid + 1
        elif word > given_word:
            high = mid - 1
        else:
            return words_string[mid]
    
    return None

    # Linear Search is slow to train!
    # for word_string in words_string:
    #     word = word_string.split()[0].lower()
    #     if word == given_word.lower():
    #         return word_string
    # return None

# if __name__ == "__main__":
#     print(get_phones("zebra"))