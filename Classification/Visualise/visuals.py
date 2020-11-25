import json
import sys
sys.path.append("./Classification")

from features_all import features_list

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
plt.style.use('ggplot')

other_sentences = json.load(open("./Corpus/Jokes/reddit_jokes.json"))[:1000]
general_sentences = open("./Corpus/General/cleaned_general.txt").readlines()[:1000]

def plot_function(function):
    print(f"Getting general data for {function.__name__} ...")
    general_values = np.array([
        function(sentence)
        for sentence in tqdm(general_sentences)])

    print(f"Getting other data for {function.__name__} ...")
    other_values = np.array([
        function(sentence)
        for sentence in tqdm(other_sentences)])
    
    _, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    ax1.hist(general_values, bins=[i for i in range(10)], edgecolor='black')
    plt.suptitle(f"{function.__name__.replace('_', ' ')} comparison: General VS Humorous", )
    ax2.hist(other_values, bins=[i for i in range(10)], edgecolor='black')
    plt.show()

    print()
    print()
    print()

if __name__ == "__main__":
    for feature in features_list:
        plot_function(feature)
