import github
import vector
from scipy.spatial import distance


def get_repo_vector(owner, repo, extension):
    words = github.get_repo_words(owner, repo, extension)
    repo_vec = vector.get_average_vector(words)

    return repo_vec


def vector_similarity(vector1, vector2):
    return 1 - distance.cosine(vector1, vector2)



if __name__ == '__main__':
    print(get_repo_vector('Kazuya-Pum', 'LineLimiter', '.js'))
