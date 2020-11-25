import json
from tqdm import tqdm

text = json.load(open('./Corpus/Jokes/reddit_jokes.json'))

order = 20

from spacy.lang.en import English
nlp = English()
tokenizer = nlp.Defaults.create_tokenizer(nlp)

unique_starters = {}

def generate_words():
    for sentence in tqdm(text):
        words_list = [token.text for token in tokenizer(sentence)][:order]

        final = ""
        for word in words_list:
            final += word + " "
        
        try:
            unique_starters[final[:-1]] += 1
        except:
            unique_starters[final[:-1]] = 1

    json.dump(unique_starters, open(f'./Generation/starters_word_{order}.json', 'w'))

def generate_characters():
    for sentence in tqdm(text):
        final = sentence[:order]
        try:
            unique_starters[final] += 1
        except:
            unique_starters[final] = 1
    
    json.dump(unique_starters, open(f'./Generation/starters_character_{order}.json', 'w'))

if __name__ == "__main__":
    generate_characters()