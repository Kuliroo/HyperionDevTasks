import spacy
nlp = spacy.load('en_core_web_md')
# Extract no. 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Extract no. 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Extract no. 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Note on similarities:
# It's hard to say anything else except for the examples mentioned in the pdf. It's interesting
# that cat and apple have less similarity than cat and banana, when none of them seem similar at all,
# but still something is "more" similar. Even with apple being closer in letters number to cat than banana.
# My example would be bar, law, client, solicitor - it shows some limits 

tokens = nlp('bar law client solicitor ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Running example file with simpler language model "en_core_web_sm":
# Similiarity between subjects in this model is higher with simple words but lesser with sentences.
# Additionally there's a UserWarning about this model not using word vectors, and basing it's similiarity
# on different elements. In my example similiarity in SM drops from .26 - .75 to .06 - .52 in MD model.