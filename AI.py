import nltk
import re

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

text="This handy tool helps you create dummy text for all your layout needs. We are gradually adding new functionality and we welcome your suggestions and feedback."
sentences = sent_tokenize(text)

text = re.sub(r"[^a-zA-Z0-9]"," ",sentences[0]) # Removes Punctuations

words = word_tokenize(text) # Tokenizes text into words
words = [w for w in words if w not in stopwords.words("english")] # Removes stopwords

print(words)