# Humor Classification

## Introduction
Humor Classification is one side of the larger idea of understanding computational humor. To accurately understand the current state of humor on social media, we turned to Reddit, as aforesaid. To the best our knowledge, this is the first time someone has used Reddit data for understanding Humor.

While there are neural techniques, using Bi-LSTMs and Transformer Models already present for classification, we opted for a more statistical and feature based approach to understand humor well.

## Features
We explored features at all the different levels:

1. Phonetic Level
We extract the phone-level information by using the CMU's phonetic dictionary, which gives the split of the word's constituents. 

Mihalcea's Paper Mentions the presence of alliterations chains as such:
"*Infants* don’t enjoy *infancy* like *adults* do *adultery*."

Upon extracting alliteration chains, we found that the examples on reddit look more like this:
"Why was the teacher cross eyed? ... Because he couldn't control his pupils."

The alliteration lies in the "why - was" and the "couldn't - control". Not as obvious, certainly.


2. Morpho-Syntactic Level
Going a level above the phonetic level we have the morphological level, where we look at the Part Of Speech (POS) tags to make the judgement. We use spacy libray's POS tagger, which is trained on a small english corpus. 

Zhang's Paper mentions the use of differences in POS ratios for verbs, nouns, pronouns, proper nouns and modifiers. We decided to explore all of them.

3. Lexico-Semantic Level
Mihalcea's Paper mentions the large amount of usage adult slang in humorous texts. The reddit taste of such kind of humor is different and we could not rely on any external tools. We decided to create a list of slang words on our own. This inclues more general terms, which we did not find commonly present in the general dataset.

"what did one muffin say to the other? ... 'whew! it's hot in this oven!'
how did the other muffin reply?
'holy shit! a talking muffin!'"

There are also hidden instances of slang. The following has not one, but two such instances:
"my sister can't stop having sex. ... i think she's addickted."

We predict this will be the largest and most weighted indicator of humor content.


We also look at antonyms pairs. This idea directly draws from the incongruity theory mentioned above. 

Example:
"*smaller* babies may be delivered by a stork  but the *bigger* heavier ones are delivered by a crane"

4. Pragmatic Level
Zhang's paper mentions the use of discourse connectives. As we are looking at reddit humor, it would seem as if these jokes are not properly formed, on the other hand, in general texts, we would find a greater coherency. Looking at the data, that is not the case; many of reddit jokes are not one-liners or even limited to 140 characters (as for tweets), since there is no such restricitve limit on reddit jokes.

Infact, due to longer jokes, we would expect a greater use of discourse connectives, to have a more proper punchline at the end.

We use hand-crafted list of popular discourse markers.

"I'd like to think that my girlfriend and I have a relationship that is above being forced to buy simple gifts as part of a made up holiday that exploits working class people through the commercialism of enormous corporations ... *But* I'd also like to get laid tomorrow night, so Walgreens after work it is."

5. Affective Level
The idea behind using affective features is that humor evokes a certain positive or negative emotion omnipresent. We use SenticNet version 6.0 to take into account the polarity of the sentence.

Examples:
"Never swallow scrabble tiles... ... That shit could spell disaster"

"Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. ... D J Trump: Fake News!"

Are some examples of negative and positive polarities.


## Experiments
Comparisions of General VS Humorous texts
![Alliteration Chain Lengths](https://i.imgur.com/eEVChpc.png)
![POS Nouns](https://i.imgur.com/HGfblSm.png)
![POS Pronouns](https://i.imgur.com/cox7xrT.png)
![POS Verbs](https://i.imgur.com/ItWwxEg.png)
![POS ProperNouns](https://i.imgur.com/z9Zj4du.png)
![Antonym Pairs](https://i.imgur.com/ZtM2mO8.png)
![Slangs](https://i.imgur.com/vbia3Nc.png)
![Absolute Polarities](https://i.imgur.com/B4H1Ema.png)
![Discourse Markers](https://i.imgur.com/KXiS3B0.png)


Running the models using scikit learn library.
| Model Used | F1 | Accuracy |
| - | - | - | 
| Logistic Regression | 0.58 | 0.605 |
| Support Vector Classifier | 0.63 | 0.62 | 
| Gaussian Naive Bayes | 0.59 | 0.625 | 

