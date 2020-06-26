"""
    Returns 1 if both query words exist in
    the document, 0 otherwise.
"""
def boolean_and(query, document):
    match_count = 0
    qlen = len(query)
    
    for w in query:
        
        if w in document:
            match_count += 1
            
        if match_count == qlen:
            return 1
        
    return 0
    

"""
    Returns 1 if at least 1 query word
    exists in the document, 0 otherwise.
""" 
def boolean_or(query, document):
    
    for w in query:
        
        if w in document:
            return 1
        
    return 0