import spacy as sy

nlp = sy.load("en_core_web_sm")

# List with Garden-path sentences:
gardenpathSentences = [
    'The cotton clothing is made of grows in Mississippi', 
    'We painted the wall with cracks', 
    'The old man the boat',
    'Mary gave the child a Band-Aid',
    'That Jill is never here hurts'
    ]

# Tokenisation and named entity recognition of each sentence, printing only entities
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text + " is a " + ent.label_)
        print(ent.label_ + " means: " + sy.explain(ent.label_))

# 1. What was the entity answer and its explanation that you looked up?
#  I have looked up PERSON and GPE entities, explained as 
# "People, including fictional" and "Countries, cities, states" respectively

# 2. Did the entity make sense in terms of the word associated with it?
# Yes.