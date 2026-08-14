from collections import Counter
sentences = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]
words = []
for sentence in sentences:
    words.extend(sentence.split())
unigram_counts = Counter(words)
total_words = len(words)
bigram_counts = Counter()
for sentence in sentences:
    tokens = sentence.split()
    for i in range(len(tokens) - 1):
        bigram = (tokens[i], tokens[i + 1])
        bigram_counts[bigram] += 1
print("Unigram Probability:")
for word in unigram_counts:
    probability = unigram_counts[word] / total_words
    print(f"P({word}) = {probability:.3f}")
print("\nBigram Probability:")
for (w1, w2), count in bigram_counts.items():
    probability = count / unigram_counts[w1]
    print(f"P({w2}|{w1}) = {probability:.3f}")
