import gensim
from sklearn.manifold import TSNE

import tsneplot.plot as plot


def load_model(path):
    return gensim.models.KeyedVectors.load_word2vec_format(path)


def _train_tsne(data):
    # find tsne coords for 2 dimensions
    tsne = TSNE(n_components=2, random_state=0)
    return tsne.fit_transform(data)


def _split_coords(arr):
    """Split array of coordinates into two arrays."""
    return arr[:, 0], arr[:, 1]


def display_words(model, words):
    close_words = []

    for w in words:
        close_words += [word for word, score in model.similar_by_word(w)]
        close_words += [w]

    Y = _train_tsne(model[close_words])

    plot.scatterplot(close_words, *_split_coords(Y))


def display_all(model):
    words = list(model.vocab.keys())
    arr = model.vectors

    Y = _train_tsne(arr)

    return plot.scatterplot(words, *_split_coords(Y))
