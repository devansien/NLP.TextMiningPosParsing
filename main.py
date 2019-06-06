import nltk

# from nltk.book import *
# from nltk.corpus import brown


# nltk basic practices
# print(brown.words()[0:10])
# print(len(brown.words()))
# print(texts())
# print(len(text1))


# nltk basic tagging practices
# sent = "I saw a boy in the park with a telescope."
# taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
# grammar = "NP: {<DT>?<JJ>*<NN>}"
# cp = nltk.RegexpParser(grammar)
# result = cp.parse(taggedS)
# print(result)
# result.draw()


# read text from file
with open('Firearms.txt', 'r') as file:
    content = file.read().replace('\n', '')

# lambda conditional (not used)
# is_noun = lambda pos: pos[:2] == 'NN'

# tokenize the content
tokens = nltk.word_tokenize(content)

# tag the content
tagged = nltk.pos_tag(tokens)

# extract target tagged word (not used)
# extracted = [word for (word, pos) in nltk.pos_tag(tokens) if is_noun(pos)]

# definite nouns
def_nouns = nltk.FreqDist(w2 for ((w1, t1), (w2, t2))
                          in nltk.bigrams(tagged)
                          if w1.lower() == "the" and t2 == "NN")

print(len(def_nouns))

# get noun list
noun_list = []
for noun in def_nouns.keys():
    noun_list.append(noun)

# sort ascending order
noun_list.sort()

# print result
print(noun_list)
