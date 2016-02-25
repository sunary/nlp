__author__ = 'sunary'


from other_tools.utils import STOP_WORDS_SET
from collections import defaultdict
from gensim import corpora, models, similarities


documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

def corpora_to_vector():
    texts = [[token.lower() for token in text.split(' ') if token.lower() not in STOP_WORDS_SET] for text in documents]

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1] for text in texts]

    dictionary = corpora.Dictionary(texts)
    print 'dictionary:'
    print dictionary.token2id

    print 'doc to bow:'
    vectors = []
    for text in texts:
        print dictionary.doc2bow(text)
        vectors.append(dictionary.doc2bow(text))

    return dictionary, vectors


def tranformation(dictionary, corpus):
    tfidf = models.TfidfModel(corpus)

    vec = [(0, 1), (4, 1)]
    print 'ftidf vector %s:' %(vec)
    print tfidf[vec]

    corpus_tfidf = tfidf[corpus]
    print 'tfidt:'
    for doc in corpus_tfidf:
        print doc

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=5)
    print 'num_topics = 2:'
    for topic in lsi.print_topics(5):
        print topic

    corpus_lsi = lsi[corpus_tfidf]
    print 'LSI 2d:'
    for doc in corpus_lsi:
        print doc


def similarity(corpus):
    tfidf = models.TfidfModel(corpus)
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)

    vec = [(0, 1), (4, 1)]
    sims = index[tfidf[vec]]
    print list(enumerate(sims))

def word_2_vector():
    pass


if __name__ == '__main__':
    dictionary, corpus = corpora_to_vector()
    tranformation(dictionary, corpus)