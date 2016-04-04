__author__ = 'sunary'


import re
import matplotlib.pyplot as plt
from gensim import corpora,models, similarities, matutils
from other_tools.utils import STOP_WORDS_SET

documents = ['The Neatest Little Guide to Stock Market Investing',
            'Investing For Dummies, 4th Edition',
            'The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns',
            'The Little Book of Value Investing',
            'Value Investing: From Graham to Buffett and Beyond',
            'Rich Dad\'s Guide to Investing: What the Rich Invest in, That the Poor and the Middle Class Do Not!',
            'Investing in Real Estate, 5th Edition',
            'Stock Investing For Dummies',
            'Rich Dad\'s Advisors: The ABC\'s of Real Estate Investing: The Secrets of Finding Hidden Profits Most Investors Miss']
ignore = ",|:|!|'"


def split(text):
    text = re.sub(ignore,'',text)
    return text.lower().split()


def atext(documents):
    texts = [[word for word in split(doc) if word not in STOP_WORDS_SET] for doc in documents]
    return texts


def to_dictionary(texts):
    dictionary = corpora.Dictionary(texts)
    # print dictionary.token2id
    return dictionary


def new_vec(doc, dictionary):
    vec = dictionary.doc2bow(split(doc))
    return vec


def index_words(texts, dictionary):
    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus


def to_matrix(corpus, num_terms):
    numpy_matrix = matutils.corpus2dense(corpus, num_terms=num_terms)
    return numpy_matrix


def cal_tfidf(corpus):
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return corpus_tfidf


def cal_lsi(dictionary, corpus_tfidf, num_topics):
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
    corpus_lsi = lsi[corpus_tfidf]
    print lsi.print_topics(2)
    return lsi, corpus_lsi


def cal_lda(dictionary, corpus_tfidf, num_topics):
    lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
    corpus_lda = lda[corpus_tfidf]
    print lda.print_topics(2)
    return lda, corpus_lda


def visualize_lsi(corpus_lsi, num_topics):
    df = {}
    for i in range(num_topics):
        df['topic_%d' % (i)] = []

    for cp in corpus_lsi:
        for i in range(num_topics):
            df['topic_%d' % (i)].append(cp[i][1])

    # df = pd.DataFrame(df)
    # print df

    plt.plot(df['topic_0'], df['topic_1'], 'ro')
    # plt.scatter(df['topic_0'], df['topic_1'])
    for i in range(len(df['topic_0'])):
        plt.annotate(str(i), (df['topic_0'][i], df['topic_1'][i]))
    plt.show()



def new_dec_lsi(doc, dictionary, lsi):
    vec_bow = dictionary.doc2bow(split(doc))
    vec_lsi = lsi[vec_bow]
    return vec_lsi


def check_sims(vec_lsi, corpus_lsi, num_terms):
    index = similarities.MatrixSimilarity(corpus_lsi, num_features=num_terms)
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item:-item[1])
    return sims


if __name__ == '__main__':
    texts = atext(documents)
    dictionary = to_dictionary(texts)
    corpus = index_words(texts, dictionary)
    corpus_tfidf = cal_tfidf(corpus)
    lsi, corpus_lsi = cal_lsi(dictionary, corpus_tfidf, 2)

    visualize_lsi(corpus_lsi, 2)

    vec_lsi = new_dec_lsi('Investing book', dictionary, lsi)
    print check_sims(vec_lsi, corpus_lsi, len(dictionary))
