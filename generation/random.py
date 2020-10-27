import random

def get_response(words_list):
    """
    Gets content words as input, generates a string of random words.
    Using for testing purposes.
    """
    if not len(words_list):
        return "This is a generic response, specially for you."
    
    response = ""
    random.shuffle(words_list)
    for word in words_list: 
        response += word + " "
    return response[:-1] + ", very cool."