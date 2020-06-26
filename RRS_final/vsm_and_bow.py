from collections import defaultdict
import numpy as np
"""
    Takes in a vocabulary and a document as a list of strings
    and returns a vector the same size as the vocabulary such that:
    
        Position i in the vector corresponds to the i-th word
        in the vocabulary and has as value the frequency
        of that word in the input document.
"""
def bag_of_words(vocabulary, document):
    bow = np.zeros(len(vocabulary), dtype=int)
    
    for w in document:
        
        if w in vocabulary:
            bow[vocabulary.index(w)] += 1
            
    return bow



"""
    Turns a list of string lists into
    a single list of all unique words.
"""
def make_corpus_wordset(corpus):
    corpus_wordset = []
    
    for doc in corpus:
        for w in doc:
            corpus_wordset.append(w)
            
    return list(set(corpus_wordset))

"""
    Make the term frequency for each word 
    in a document.
    
    Returns a defaultdict as {word : TF}
"""
def make_tf_dict(document):
    tf_dict = defaultdict(float)
    n = len(document)
    
    for w in document:
        tf_dict[w] += 1/n 
           
    return tf_dict
"""
    Make the inverse document frequency for each word
    word in a corpus using the vocabulary.
    
    IDF = number of docs a word appears in / number of docs in corpus
    
    Returns a defaultdict as {word : IDF}.
"""
def make_idf_dict(corpus):
    N = len(corpus)
    corpus_wordset = make_corpus_wordset(corpus)
    
    idf_dict = defaultdict(float)
    
    for w in corpus_wordset:
        
        for d in corpus:
            
            if w in d:
                idf_dict[w] += 1 / N
    
    return idf_dict

def make_tf_idf_dict(tf_dict, idf_dict):
    tf_idf_dict = defaultdict(float)
    
    for word in tf_dict:
        tf_idf_dict[word] = tf_dict[word] * idf_dict[word]
        
    return tf_idf_dict

"""
    Uses a tf-idf dictionary belonging
    to a query or document and makes
    a vector form.
    
    i-th position in the vector corresponds
    with i-th word in the vocabulary and
    the value is the corresponding tf-idf value.
"""
def make_vector_form(vocabulary, tf_idf_dict):
    word_vec = np.zeros(len(vocabulary), dtype=float)
    
    for i, word in enumerate(vocabulary):
        word_vec[i] = tf_idf_dict[word]
        
    return word_vec