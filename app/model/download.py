import gensim.downloader as api
import os

if __name__ == '__main__':
    name = 'word2vec-google-news-300'
    model = api.load(name)
    model.save(os.path.join(os.path.dirname(__file__), f'{name}.kv'))
