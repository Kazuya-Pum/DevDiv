from .github import *
from .vector import *
from scipy.spatial import distance


def get_repo_vector(owner, repo, extension):
    words = get_repo_words(owner, repo, extension)
    repo_vec = get_average_vector(words)

    return repo_vec


def vector_similarity(vector1, vector2):
    return 1 - distance.cosine(vector1, vector2)
