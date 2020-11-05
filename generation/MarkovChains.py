import random

text = [
    "this is a random sentence.",
    "this is another dumb sentence.",
    "the cats are on the mats.",
    "the dog is chasing the cat.",
    "the apple is on the table.",
    "the bat hits the ball.",
    "this is an example of a unique sentence."
    "these are to be used for testing purposes only.",
]

def combine_words(words_list, i, j):
    combined = ""
    for x in range(i, j):
        combined += words_list[x] + " "
    return combined[:-1]

def markovify(level='character', order=3, text=text):
    ngrams = {}

    if level == 'character':
        for sentence in text:
            l = len(sentence)
            for i in range(l-order):
                if sentence[i:i+order] not in ngrams.keys():
                    ngrams[sentence[i:i+order]] = []
                ngrams[sentence[i:i+order]].append(sentence[i+order])
    
    elif level == 'word':
        for sentence in text:
            words_list = sentence.split()
            for i in range(len(words_list)-order):
                if words_list[i] not in ngrams.keys():
                    ngrams[combine_words(words_list, i, i+order)] = []
                ngrams[combine_words(words_list, i, i+order)].append(words_list[i+order])

    return ngrams

def generate_text(ngrams, level='character', order=3, seed_text="the"):
    result = seed_text.strip()
    if level == 'character':
        while result[-1] != '.':
            try:
                temp = random.choice(ngrams[result[-order:]])
            except:
                temp = '.'
            result += temp
    else:
        while result[-1] != '.':
            try:
                word_list = result.split()                
                temp = " " + random.choice(
                    ngrams[combine_words(word_list, len(word_list)-order, len(word_list))]
                )
            except:
                break
            result += temp
        

    return result

# if __name__ == "__main__":
#     level = 'word'
#     order = 4
#     ngrams = markovify(level, order, text=text)
#     print(generate_text(ngrams, level, order, seed_text="the cats are on"))
