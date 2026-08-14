from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
new_text="i am studying nlp "
ex_words=word_tokenize(new_text)
for w in ex_words:
    print(ps.stem(w))