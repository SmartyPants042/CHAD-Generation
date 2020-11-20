from Helpers.cmu_interface import get_phones
from ntlk.corpus import wordnet as wn

def sentence_length(sentence):
    return len(sentence)

def alliteration_chain_length(sentence):
    """
    returns the total length of the alliteration chains, combined
    """
    sentence = sentence + " ."
    count = 0
    words_list = sentence.split()
    prev_phone = None
    temp = []
    for i in range(0, len(words_list)):
        # we take the first phone
        try:
            phone = get_phones(words_list[i])[0]
        except:
            phone = None
        
        # extraction logic
        if prev_phone and prev_phone == phone:
            temp.append(words_list[i-1])
        elif prev_phone:
            if len(temp):
                count += len(temp) + 1
            temp = []
        prev_phone = phone
    return count

def antonym_pairs(sentence):
    pass

features_list = []
features_list.append(sentence_length)
features_list.append(alliteration_chain_length)

if __name__ == "__main__":
    # print(alliteration_chain_length("apples apples good good goody"))
    pass