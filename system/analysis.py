import pandas as pd

class Analysis():
    def __init__(self, repository):
        self.words = pd.Series(repository.words)
        self.raw_words = pd.Series(repository.raw_words)


    def get_vocabulary_count(self):
        return self.words.value_counts()


    def get_most_used_word(self):
        return self.words.value_counts().index[0]