import re
from collections import Counter, defaultdict
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
for sent in sentences:
    unigram_counts.update(sent[:-1])
    for i in range(len(sent) - 1):
        bigram_counts[(sent[i], sent[i + 1])] += 1
vocab = sorted(set(unigram_counts))
probability_matrix = defaultdict(dict)
for w1 in vocab:
    for w2 in vocab:
        probability_matrix[w1][w2] = (
            bigram_counts[(w1, w2)] / unigram_counts[w1]
            if unigram_counts[w1]
            else 0
        )
print("BIGRAM PROBABILITY MATRIX")
print(f"{'Word':<10}", end="")
for word in vocab:
    print(f"{word:<10}", end="")
print()
print("-" * (10 + 10 * len(vocab)))
for w1 in vocab:
    print(f"{w1:<10}", end="")
    for w2 in vocab:
        print(
            f"{probability_matrix[w1][w2]:<10.2f}",
            end=""
        )
    print()