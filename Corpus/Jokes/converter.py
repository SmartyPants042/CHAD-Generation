import json

dataset = json.load((open('./Corpus/Jokes/cleaned_jokes.json')))
sentences = []

for data_sample in dataset:
    sentences.append(data_sample['setup'] + " ... " + data_sample['punch'])

with open('./Corpus/Jokes/reddit_jokes.json', 'w') as f:
    json.dump(sentences, f)