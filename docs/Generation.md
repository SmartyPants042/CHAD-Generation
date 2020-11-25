# Humor Generation
Generating is not a trivial task

## Markov Chains
Here, we combine the power of probabilistic stochastic models with n-grams. We look at both the word and the character level for generation, and each time, look at a sequence of 'n' such characters/words. This gives us an idea of the transition probabilities, for each such sequence. We look at empirical evidence to get a better understanding of the models.

We start with the character level, that is, looking at n characters in a sequence and predicting the next character with the highest probability as seen in the reddit jokes corpus.
for n = 2, we see that the results are not very promising, and the sequences terminate early.
A.
I.

However, as we go from n = 3 to n = 6, we see a consistent improvement in the quality of the jokes; in terms of grammatical correctness, logical sense and the spelling.

n = 3 - incorrect spellings
Why daisinguids of my partionald there you could him.

n = 4 - correct spellings, incorrect grammar 
What didn't like answer culture.

Knock Knights for put these doctors on to probably.


character level, n = 5 - better grammar
Why couldn't under 10 million date? .
I have in my life said in one of Democracy" .

character level, n = 6 - longer sequences still fail
What do you know that shit got two gay man is a duck say to ruin a joke a lightbulb? .
Did you hear about the floor of things Dickens wear glass clown.
Went to say really *stepped on the explodes white.


n = 12 - still no logical sense
What did the physicists so bad at soccer? .
TUMBLR ... What she didn't want to interrupt her.

n = 20 - grammar correct, but the logical sense and coherency still missing
What I'm doing to occupy my free time now that the majority of car accidents happen in Russia.

Thank you student loans, for helping me get through college ... I don't think the speed was why I was arrested though...

What's the difference between Rosh Hashanah and Yom Teruah?"  
And he said to me, he said:  
"Oh, about fifty bucks."...


Also, observe that for n = 20, we are able to complete the quotes, which is missing for n <= 6; there are * or " left incomplete, due to such small n.


We now proceed to the word level, where we do not need to worry about the spellings, and can hope for a better understanding of grammar.

n = 2 - grammar correct, but no logical sense ...
"A friend of mine asked if I should use to cut by . "

n = 3
"Teacher : All Idiots Stand Up A boy stand up Teacher : so are you familiar with my parodies ? Yeah my PAIR O DEEZ NUTS ! !"

The above was the BEST in terms of the quality of the joke. There are a bit of minor corrections still that can be done. Upon digging throught the dataset, we find its the child of the below jokes:
    
    "Teacher: All Idiots Stand Up A boy stand up Teacher: so are you an idiot ? Boy: No I can't bear you standing alone madam... ... "

    "What is Weird Al Yankovic's favorite pick up line? ... Hey, so are you familiar with my parodies? Yeah my PAIR O DEEZ NUTS!!!",

Word level, N = 4
"Why are there so many trees along the Champs - Élysées ? ... Because ze Germans like to march in ze shade ."

"I was going to buy some classical CDs ... ... But it just came up with " Page not found " ."

"My favorite joke in Polish I will try to upload one each day . Just look for johnfromnorway 

https://i.imgur.com/j1poxyK.jpg"

"What 's the difference between a hippie chick and a hockey player ? ... A hockey player showers after three periods ."

"What do you call a midget with Down Syndrome? ... you call him a little slow"

At this point the jokes make perfect logical sense, along with grammatical rules followed. However, at this point, the n became so large, that the jokes were repetetive.


## Word Level LSTM
Neural Techniques for text generation are very popular. Especially with the coming of BERT and GPT-3 Transformer Models. However, since they are much of a black-box, we decided to test out humor generation using a Word level LSTM Model written in PyTorch.

Our end goal was to generate humorous texts, and since models learn from the Reddit Data Corpus, we expect that the jokes are similar in style to the Reddit taste of humor.

We first start with pre-processing our data, using spacy's tokenizer. Then, we turn our attention to word embeddings. We wanted to look at the differences of using Word2Vec versus training our own embeddings. 
Below is the model architecture:

Embedding Layer 
-- (converts words to machine understandable vectors)-->
LSTM Layer 1
-- (converts vector to internal meaning representations) -->
LSTM Layer 2
-- (Extracts and goes to a greater depth of relations) -->
Linear Layer
-- (Converts Sequential Data in output ready format) --|

The reason for using two lstm layers stacked on top of each other is that while the first one extracts the word-level meanings, we can go a level beyond and look at sentence level abstractions in the second layer.

## Experiments
We observed the very high training time, even after reducing the dataset size. This is due to the sequential nature of LSTM cells, where nth cell requires data from all the previous (n-1) cells. There are very little optimizations that can be done; and the training time can range upto 30 minutes per epoch.

Below is our hyperparameter configuration that we use to generate the jokes:

The sequence length controls how many words the model sees, before predicting the next word. The lesser it it, the more grammatically incorrect the sequence becomes. On the other hand, increasing it too much causes overfitting; the jokes become repetitive.
SEQUENCE_LENGTH = 3

The number of times our model sees the entire data
EPOCHS = 4

The size of samples it sees at once. 32 for GPU level optimizations
BATCH_SIZE = 32

The architecture of the model, as described above. Droput is percentage of cells that are temporarily put on hold, for a particular iteration. This prevents overfitting. 
MODEL_CONFIG = {
    'pre_embed': True,
    'embedding_dim': 100,
    'lstm_cells': 100,
    'lstm_num_layers': 2,
    'lstm_dropout': 0.2
}

The size of the generated joke
PREDICTION_SIZE = 20

![Model Accuracy](https://i.imgur.com/k2w2HKP.png)


Generated Samples:
"Knock knock . Who s there ? Someone wo n't get an battery toilet ? ... The NBA says to down and Hilary old time."

"Knock knock . Who s there ?     I was knot . " I 'll understand to feminists . Sign child out there take up prefer" 
