from .github import Repository
from .vector import *
from scipy.spatial import distance


def vector_similarity(vector1, vector2):
    return 1 - distance.cosine(vector1, vector2)


def execute(owner, repo, extension):
    repository = Repository(owner, repo, extension)
    return get_average_vector(repository.words)