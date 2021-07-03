from gensim.models import KeyedVectors
import os
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), 'model', 'word2vec-google-news-300.kv')
wv = KeyedVectors.load(model_path)


def get_average_vector(words):
    vectors = np.zeros((len(wv[0]),), dtype=np.float)

    for word in words:
        if word in wv:
            vectors = np.add(vectors, wv[word])

    if len(vectors) > 0:
        vectors = np.divide(vectors, len(vectors))

    return vectors
