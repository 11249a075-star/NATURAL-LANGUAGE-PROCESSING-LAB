from collections import Counter
sentences = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]
unigram_counts = Counter()
bigram_counts = Counter()
for sentence in sentences:
    words = sentence.split()
    unigram_counts.update(words)
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_counts[bigram] += 1
def sentence_probability(sentence):
    words = sentence.split()
    probability = 1
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        if bigram_counts[(w1, w2)] == 0:
            return 0
        probability *= bigram_counts[(w1, w2)] / unigram_counts[w1]
    return probability
s1 = "I like NLP"
s2 = "Python like I"
p1 = sentence_probability(s1)
p2 = sentence_probability(s2)
print("Sentence 1:", s1)
print("Probability:", p1)
print("\nSentence 2:", s2)
print("Probability:", p2)
if p1 > p2:
    print("\nMore probable sentence:", s1)
elif p2 > p1:
    print("\nMore probable sentence:", s2)
else:
    print("\nBoth sentences have equal probability.")
