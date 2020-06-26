from auxilary_functions import *
from rank_bm25 import BM25Okapi

class RRS:
    def __init__(self, method):
        self.method = method
        self.corpus = None
        
        
    def rank(self, query, old_ranking, old_ranking_format):
        
        if old_ranking_format == 'xml':
            self.corpus = handle_geonetwork_xml(old_ranking)

            if self.method == 'bm25':
                abstract_corpus, keyword_corpus = make_corpus(self.corpus)
                bm250kapi = BM25Okapi(abstract_corpus)
                scores = bm250kapi.get_scores(query)
                
                new_ranking = sorted([ (scores[i], x['url']) for i, x in enumerate(self.corpus)], key=lambda tup: tup[0])
                new_ranking.reverse()
                
                return new_ranking
              
        
    def insert_feedback(self, feedback):
        
        if self.method == 'BM250kapi':
            return 'current ranking method has not feedback learning mechanism, please make a different instance of RRS with a learning method'
        
        if self.method == 'blabla':
            return 'blablalba..'