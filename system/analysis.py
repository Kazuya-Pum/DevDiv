import pandas as pd

class Analysis():
    def __init__(self, repository):
        self.words = pd.Series(repository.words)
        self.raw_words = pd.Series(repository.raw_words)

    # 変数の最大文字数とその文字
    def var_max_len(self):

        unique_len_list = [len(i) for i in self.raw_words.unique()]
        unique_dict = dict(zip(self.raw_words.values, unique_len_list))
        sort_value = max(unique_dict.items(), key=lambda x:x[1])
        print(sort_value)

        return sort_value

    def var_mean_len(self):

        
        unique_list = self.raw_words.unique()
        unique_len = len(unique_list)
        # len(''.join(unique_list))/unique_len # 文字の長さ
        
        # words_len = len(self.raw_words)
        # print(len(''.join(self.raw_words.values))/words_len) # 文字の長さ
        # print(self.words.unique()) #  
        # print(len(self.words.unique())) # 

        return len(''.join(unique_list))/unique_len
    
    def var_kind(self):

        
        unique_list = self.raw_words.unique()
        unique_len = len(unique_list)
        # len(''.join(unique_list))/unique_len # 文字の長さ
        
        # words_len = len(self.raw_words)
        # print(len(''.join(self.raw_words.values))/words_len) # 文字の長さ
        # print(self.words.unique()) #  
        # print(len(self.words.unique())) # 

        return unique_len

    # 変数の数
    def var_num(self):

        # print(len(self.raw_words.values))

        return len(self.raw_words.values)

    def get_vocabulary_count(self):
        return self.words.value_counts()


    def get_most_used_word(self):
        return self.words.value_counts().index[0]