from collections import Counter
sentences = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]
print("Grammar-Based Model")
def grammar_check(sentence):
    words = sentence.split()
    if len(words) != 3:
        return False
    subject = ["I"]
    verb = ["like", "study"]
    obj = ["NLP", "Python"]
    return words[0] in subject and words[1] in verb and words[2] in obj
test1 = "I like NLP"
test2 = "Python like I"
print(test1, ":", grammar_check(test1))
print(test2, ":", grammar_check(test2))
print("\nStatistical Model")
unigram = Counter()
bigram = Counter()
for sentence in sentences:
    words = sentence.split()
    unigram.update(words)
    for i in range(len(words)-1):
        bigram[(words[i], words[i+1])] += 1
def bigram_probability(sentence):
    words = sentence.split()
    prob = 1
    for i in range(len(words)-1):
        if bigram[(words[i], words[i+1])] == 0:
            return 0
        prob *= bigram[(words[i], words[i+1])] / unigram[words[i]]
    return prob
print(test1, "Probability =", bigram_probability(test1))
print(test2, "Probability =", bigram_probability(test2))
