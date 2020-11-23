import json
import sys
sys.path.append("./Classification")

from features_all import (
    alliteration_chain_length, 
    antonym_pairs,
    discourse_markers,
    polarity,
    absolute_polarity,
    all_slangs
)
    
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

other_sentences = json.load(open("./Corpus/Jokes/reddit_jokes.json"))
general_sentences = open("./Corpus/General/general.txt").readlines()

def plot_function(function):
    general_values = np.array([
        function(sentence) 
        for sentence in general_sentences])

    other_values = np.array([
        function(sentence) 
        for sentence in other_sentences])
    
    _, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    ax1.hist(general_values, bins=[i for i in range(10)], edgecolor='black')
    plt.suptitle(f"{function.__name__.replace('_', ' ')} comparison: General VS Humorous", )
    ax2.hist(other_values, bins=[i for i in range(10)], edgecolor='black')
    plt.show()

if __name__ == "__main__":
    plot_function(all_slangs)
