import re
from nltk import FreqDist
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
fdist = FreqDist(words)
total_words = len(words)
print(f"{'Word':<15}{'Count':<10}{'Probability':<15}")
print("-" * 40)
for word, count in fdist.items():
    probability = count / total_words
    print(f"{word:<15}{count:<10}{probability:<15.4f}")