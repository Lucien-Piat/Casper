def oneWord(sequence, start, wlen):
    for i in sequence :
        w = seq[start: start+wlen]
    return w
seq='ABCDEFGHIJKLM'
s = oneWord(seq,4,5) # "EFGHI"
print(s)


def countWord(sequence, word):
    wlen = len(word)
    for i in range(wlen) :
        w = oneWord(sequence,i, wlen)
        n = 0
        if w == word : 
            n = n +1 
    return n 

phrase='LESCHAUSSETTESDELARCHIDUCHESSESONTELLESSECHES'
num = countWord(phrase,'SSE') # 3
print(num)