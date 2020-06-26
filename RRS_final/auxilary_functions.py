import string
import xmltodict


"""
    Takes in geonetwork xml ranking output.
    
    Outputs a list of documents represented
    as dictionaries.
    
    The list is ordered according to the
    geonetwork ranking.
"""
def make_doclist(geonetwork_output_xml):
    
    with open(geonetwork_output_xml) as fd:
        doc = xmltodict.parse(fd.read())
        
    return [dict(d) for d in dict(doc['response'])['metadata']]

"""
    Collect relevant information from a single
    document dictionary into a new dictionary.
    
    The slimmer representation only takes the 
    abstract, keyword set and url.
"""
def make_clean_doc(document):
    keys = document.keys()
    
    clean_doc = {}
    
    clean_doc['abstract'] = document['abstract'] # single string
    clean_doc['keywords'] = document['keyword'] # list of keyword

    if 'identifier' in keys:
        clean_doc['url'] = document['identifier'] # link to the dataset

    elif 'link' in keys:
        clean_doc['url'] = document['link']
    
    return clean_doc

"""
    Turns al the documents from a geonetwork ranking
    into the slimmer representation.
    
    Output is the same ordering as geonetwork gives.
"""
def clean_doclist(doclist):
    docset = [None] * len(doclist)
    
    for i, d in enumerate(doclist):
        docset[i] = make_clean_doc(d)
    
    return docset

def handle_geonetwork_xml(geonetwork_output_xml):
    return clean_doclist(make_doclist(geonetwork_output_xml))

"""
    Turns a clean doclist into a list of lists where
    each sublist represents a document and each element
    in the sublist is a string that exists in the document.
    
    Returns a one corpus for all the dataset abstracts
    and one for all the keyword lists.
"""
def make_corpus(clean_doclist):
    abstracts = [None] * len(clean_doclist)
    keywords = [None] * len(clean_doclist)
    
    for i, d in enumerate(clean_doclist):
        
        abstract = clean_doclist[i]['abstract'].split()        
        abstracts[i] = [clean_word(x) for x in abstract]
        keywords[i] = clean_doclist[i]['keywords']  
        
    return abstracts, keywords

"""
    Remove punctuations marks and makes a string
    only lower case.
"""
def clean_word(word):
    
    for char in string.punctuation + '“':
        word = word.replace(char, '')
        
    return word.lower()


"""
    Turns a clean document list (list of dictionaries)
    as made by the handle_geonetwork_xml function and
    makes a single list of all words in it. This list
    is used as a dictionary to create the bags of words.
"""
def make_vocabulary(clean_doclist):
    doclist = handle_geonetwork_xml('output_climate.xml')
    vocab = []
    
    for x in doclist:
        
        for w in x['abstract'].split():
            vocab.append( clean_word(w) )
            
        for w in x['keywords']:
            vocab.append( clean_word(w) )
        
    return list(set(vocab))