import json
import sys
sys.path.append("./Classification")

from features_all import features_list

import matplotlib.pyplot as plt

other_sentences = json.load(open("./Corpus/Jokes/reddit_jokes.json"))[:10000]
general_sentences = open("./Corpus/General/general.txt").readlines()[:10000]    


for feature in features_list:
    pass
