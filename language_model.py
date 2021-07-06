import nltk
import os
import io
import re
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize, sent_tokenize 
from nltk.lm import MLE

class LanguageModel():

    def __init__(self):
        if os.path.isfile('movies_text.txt'):
            with io.open('movies_text.txt', encoding='utf8') as fin:
                text = fin.read()

        tokenized_text = [list(map(str.lower, word_tokenize(sent))) 
              for sent in sent_tokenize(text)]   
        # 3 for trigram
        n = 3
        train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
        self.model = MLE(n) 
        self.model.fit(train_data, padded_sents)

    def predict(self, list_of_words):
        return self.model.generate(text_seed=list_of_words)


language_model = LanguageModel()
predicted_text = language_model.predict(["I", "am", "very"])
print(predicted_text)
