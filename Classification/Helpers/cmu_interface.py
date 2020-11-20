f = open('./Classification/Helpers/CMU_dict')
words_string = f.readlines()

def get_phones(given_word):
    for word_string in words_string:
        if word_string.split()[0].lower() == given_word.lower():
            return word_string
    return None
