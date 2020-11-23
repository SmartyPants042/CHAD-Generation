sentences = open("./Corpus/General/general.txt").readlines()

cleaned_sentences = []

count = 0
for sentence in sentences:
    temp = sentence.split()
    if not( not len(temp) \
        or sentence[0] == '[' \
        or temp[0] == "CHAPTER" \
        or temp[0] == "VOLUME"):
        cleaned_sentences.append(sentence)
    
print(len(cleaned_sentences))
open("./Corpus/General/cleaned_general.txt", 'w').writelines(cleaned_sentences)
