# Program which changes every second letter first, and then every second word to upper case.

# User input of a sentence, program makes each alternate character lower case:
user_sentence = input("Please write down a random sentence: ")
snake_sentence = ""

# Every second letter becomes lower case:
for x in range(len(user_sentence)):
    
    if x % 2 == 1:
        snake_sentence += user_sentence[x].lower()
    else:
        snake_sentence += user_sentence[x].upper()

print(snake_sentence)

# Every second word becomes upper case:

split_sentence = user_sentence.split()
final_split_sentence = []

for y in range(len(split_sentence)):

    if y % 2 == 0:
        final_split_sentence.append(split_sentence[y].lower())
    else:
        final_split_sentence.append(split_sentence[y].upper())

print(" ".join(final_split_sentence))