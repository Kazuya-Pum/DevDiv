from .github import Repository
from .analysis import Analysis
# from .vector import *
from scipy.spatial import distance


def vector_similarity(vector1, vector2):
    return 1 - distance.cosine(vector1, vector2)


def execute(owner, repo, extension):
    repository = Repository(owner, repo, extension)
    analysis = Analysis(repository)

    vec_type = "vec_type"   #TODO
    word_type = "word_type"
    most_used = analysis.get_most_used_word()

    res = f'{vec_type}型の{word_type}な{most_used}の使い手'

    return {'res': res, 'text': ' '.join(repository.words)}