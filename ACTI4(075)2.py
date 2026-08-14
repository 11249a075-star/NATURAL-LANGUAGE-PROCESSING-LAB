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
        bigram_counts[(words[i], words[i + 1])] += 1
vocabulary = set(unigram_counts.keys())
V = len(vocabulary)
def laplace_probability(sentence):
    words = sentence.split()
    probability = 1
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        count_bigram = bigram_counts[(w1, w2)]
        count_unigram = unigram_counts[w1]
        prob = (count_bigram + 1) / (count_unigram + V)
        probability *= prob
    return probability
s1 = "I like NLP"
s2 = "Python like I"
p1 = laplace_probability(s1)
p2 = laplace_probability(s2)
print("Sentence 1:", s1)
print("Laplace Probability:", p1)
print("\nSentence 2:", s2)
print("Laplace Probability:", p2)
if p1 > p2:
    print("\nMore probable sentence:", s1)
else:
    print("\nMore probable sentence:", s2)
