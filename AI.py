import nltk
import re
nltk.download("stopwords")

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


text="This handy tool helps you create dummy text for all your layout needs. We are gradually adding new functionality and we welcome your suggestions and feedback."

sentences = sent_tokenize(text)
# print(sentences[1])

#punctuation remover
text = re.sub(r"[^a-zA-Z0-9]"," ",sentences[0])

words = word_tokenize(text)
words = [w for w in words if w not in stopwords.words("english")]

print(words)