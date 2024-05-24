from collections import Counter
def solution(s):
    
    if Counter(s.lower())['y']!=Counter(s.lower())['p']:
        return False
    return True