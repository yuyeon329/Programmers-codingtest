import re

def solution(files):
    tmp = [re.split(r"([0-9]+)",i) for i in files]
    j = sorted(tmp, key = lambda x: (x[0].upper(), int(x[1])))
    
    return ["".join(k) for k in j]
