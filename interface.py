from nltk.tokenize import word_tokenize 

from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english')) 

# getting generation methods
from generation.random import get_response 

def get_inputs():
    user_input = input()
    return user_input

def filter_sentence(sentence):
    """
    Currently uses only stop words to 
    """
    
    filtered_sentence = [
        word for word in word_tokenize(sentence) 
        if word not in stop_words
    ]
    return filtered_sentence

if __name__ == "__main__":
    user_input = get_inputs()
    words_list = filter_sentence(user_input)
    response = get_response(words_list)

    print(response)