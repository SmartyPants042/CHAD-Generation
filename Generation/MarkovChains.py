import random
import json
from tqdm import tqdm
from spacy.lang.en import English
nlp = English()
tokenizer = nlp.Defaults.create_tokenizer(nlp)

text = json.load(open('./Corpus/Jokes/reddit_jokes.json'))

def combine_words(words_list, i, j):
    combined = ""
    for x in range(i, j):
        combined += words_list[x] + " "
    return combined[:-1]

def markovify(level='character', order=3, text=text):
    ngrams = {}

    if level == 'character':
        for sentence in tqdm(text):
            l = len(sentence)
            for i in range(l-order):
                if sentence[i:i+order] not in ngrams.keys():
                    ngrams[sentence[i:i+order]] = []
                ngrams[sentence[i:i+order]].append(sentence[i+order])
    
    elif level == 'word':
        for sentence in tqdm(text):
            words_list = [token.text for token in tokenizer(sentence)]
            for i in range(len(words_list)-order):
                if words_list[i] not in ngrams.keys():
                    ngrams[combine_words(words_list, i, i+order)] = []
                ngrams[combine_words(words_list, i, i+order)].append(words_list[i+order])

    return ngrams

def generate_text(ngrams, level='character', order=3, seed_text="the", limit=100):
    result = seed_text.strip()
    if level == 'character':
        for _ in range(limit):
            try:
                temp = random.choice(ngrams[result[-order:]])
            except:
                temp = '.'
            result += temp
    else:
        for _ in range(limit):
            try:
                word_list = [token.text for token in tokenizer(result)]
                temp = " " + random.choice(
                    ngrams[combine_words(word_list, len(word_list)-order, len(word_list))]
                )
            except:
                break
            result += temp

    return result

if __name__ == "__main__":
    train = int(input("Train? (0 = no, else = yes): "))
    # train = False
    if train:
        level = 'character'
        order = 20
        ngrams = markovify(level, order, text=text)
        json.dump(ngrams, open(f'./Generation/ngrams_{level}_{order}.json', 'w'))
    else:
        print("Loading Model ... ", end="")
        level = 'character'
        order = 20
        ngrams = json.load(open(f'./Generation/ngrams_{level}_{order}.json', 'r'))
        print("Done!")

    try:
        starters = json.load(open(f'./Generation/starters_{level}_{order}.json'))
    except:
        raise FileNotFoundError("Need to run the seed_generation.py file first")
    wts = [starters[sentence] for sentence in starters]
    seed_text = random.choices([sentence for sentence in starters], weights=wts)[0]

    print(generate_text(ngrams, level, order, seed_text))
