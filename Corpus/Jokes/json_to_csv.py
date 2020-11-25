import pandas as pd
import json

f = open('reddit_jokes.json')
data = json.load(f)
df = pd.DataFrame(data)
df.to_csv('reddit_jokes.csv')
