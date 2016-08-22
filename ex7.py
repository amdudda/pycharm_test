# use a dictionary to check if duplicates exist in a wordlist
wordlist = ["a","ba","ca","ba"]

def has_duplicates(wordlist):
    d = dict()
    for w in wordlist:
        if w not in d:
            d[w] = 0
        else:
            return True
    return False

print(has_duplicates(wordlist))