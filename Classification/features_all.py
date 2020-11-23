from Helpers.cmu_interface import get_phones
from Helpers.discourse_markers import formal_markers, informal_markers
from Helpers.SenticNet.senticnet6_polarity import senticnet6
from Helpers.slang import slangs
from string import punctuation as puncts
from nltk.corpus import wordnet as wn

import spacy
nlp = spacy.load("en_core_web_sm")

features_list = []

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
    """
    Takes in a sentence and returns the length
    of the list of tuples with all antonyms pairs
    """
    allantons = []
    sentence = sentence.lower().strip()
    for i in puncts:
        sentence = sentence.replace(i,'')
    words = sentence.split(' ')
    end = len(words)
    for i in range(end-1):
        for j in range(i+1,end):
            w1, w2 = words[i], words[j]
            w1s, w2s = wn.synsets(w1), wn.synsets(w2)
            for x in w1s:
                for y in w2s:
                    xarr = x.lemmas()
                    yarr = y.lemmas()
                    for p in xarr:
                        for q in p.antonyms():
                            if q in yarr:
                                thing = (w1,w2)
                                if thing not in allantons:
                                    allantons.append(thing)
    return len(allantons)

def POS_verbs_ratio(sentence):
    total = len(sentence.split())
    doc = nlp(sentence)
    
    count = 0
    for token in doc:
        if token.pos_ == "VERB":
            count += 1
    
    return round(count/total, 3)

def POS_proper_nouns_ratio(sentence):
    total = len(sentence.split())
    doc = nlp(sentence)
    
    count = 0
    for token in doc:
        if token.pos_ == "PROPN":
            count += 1
    
    return round(count/total, 3)

def POS_nouns_ratio(sentence):
    total = len(sentence.split())
    doc = nlp(sentence)
    
    count = 0
    for token in doc:
        if token.pos_ == "NOUN":
            count += 1
    
    return round(count/total, 3)

def POS_pronouns_ratio(sentence):
    total = len(sentence.split())
    doc = nlp(sentence)
    
    count = 0
    for token in doc:
        if token.pos_ == "PRON":
            count += 1
    
    return round(count/total, 3)

def discourse_markers(sentence):
    """
    returns the count of how many discourse markers are used
    """
    count = 0
    for marker in informal_markers:
        if marker in sentence:
            count += 1

    for marker in formal_markers:
        if marker in sentence:
            count += 1
    
    return count

def polarity(sentence):
    """
    returns the sum of the polarities from SenticNet
    """
    score = 0
    for word in sentence.split():
        try:
            score += senticnet6[word]
        except:
            pass
    return score

def absolute_polarity(sentence):
    """
    returns the absolute sum of the polarities from SenticNet
    """
    score = 0
    for word in sentence.split():
        try:
            score += abs(senticnet6[word])
        except:
            pass
    return score

def all_slangs(sentence):
    sentence = sentence.lower()
    count = 0
    for slang in slangs:
        if slang in sentence:
            count += 1
    
    return int(bool(count))

features_list.append(sentence_length)
features_list.append(alliteration_chain_length)
features_list.append(POS_nouns_ratio)
features_list.append(POS_pronouns_ratio)
features_list.append(POS_verbs_ratio)
features_list.append(POS_proper_nouns_ratio)
features_list.append(discourse_markers)
features_list.append(polarity)
features_list.append(absolute_polarity)
features_list.append(all_slangs)

# if __name__ == "__main__":
#     print(alliteration_chain_length("apples apples good good goody"))
#     print(POS_verbs_ratio("The gorilla ate the banana."))
#     print(POS_nouns_ratio("The gorilla ate the banana."))
#     print(POS_pronouns_ratio("The gorilla ate the banana. He was hungry."))
#     print(POS_proper_nouns_ratio("Will Smith ate the banana."))

