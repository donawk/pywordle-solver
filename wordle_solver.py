
import english_words as ew
words = ew.english_words_lower_alpha_set
nw = list(filter(lambda x: len(x) == 5, words))

SPACES = [' ', '_']
DIV = ','

def best_guess(w, n, v):
    letters = [{}, {}, {}, {}, {}]
    pos_max = [0, 0, 0, 0, 0]
    word_count = len(w)
    for word in w:
        for i, l in enumerate(word):
            pos = letters[i]
            if l in pos.keys():
                count = pos[l] + 1
                pos[l] = count
            else:
                count = 1
                pos[l] = count
            #if count > pos_max[i]: pos_max[i] = count # could just add one, maybe
    word_ratings = {}
    for word in w:
        if v: print(word)
        score = 0.0
        for i, l in enumerate(word):
            pos_count = letters[i][l]
            score = score + (pos_count / word_count)
            if v: print(f"({l} - score: {score:.2f}\t{pos_count} / {word_count}")
        word_ratings[word] = score
    ranked_words = list(reversed(sorted(word_ratings, key=lambda x: word_ratings[x])))
    if v:
        for letter in letters:
            print(letter)

    for word in ranked_words[:n]:
        print(word, format(word_ratings[word], '.3f'))

def some(w, p):
    if DIV in p:
        end = p.index(DIV)
        for i, l in enumerate(p[:end]):
            if l not in SPACES:
                w = list(filter(lambda x: x[i] == l, w))
        return some(w, p[(end+1):])
    else:
        for i, l in enumerate(p):
            if l not in SPACES:
                w = list(filter(lambda x: x[i] == l, w))
        return w

def wrong(w, p):
    if DIV in p:
        end = p.index(DIV)
        for i, l in enumerate(p[:end]):
            if l not in SPACES:
                w = list(filter(lambda x: x[i] != l, w))
        return wrong(w, p[(end+1):])
    else:
        for i, l in enumerate(p):
            if l not in SPACES:
                w = list(filter(lambda x: x[i] != l, w))
        return w

def notin(w, n):
    for l in n:
        w = list(filter(lambda x: l not in x, w))
    return w

def isin(w, f):
    for l in f:
        w = list(filter(lambda x: l in x, w))
    return w

'''
def some(w, p):
    for i, l in enumerate(p):
        if l not in SPACES:
            w = list(filter(lambda x: x[i] == l, w))
    return w
'''

        
def solver():
    w = nw[:]
    found = False
    while not found:
        w = some(w, input("What is the format? ").lower())
        w = wrong(w, input("What is the wrong format? ").lower())
        w = notin(w, input("What letters aren't in it? ").lower())
        w = isin(w, input("What letters are in it? ").lower())
        show = input(f"You have {len(w)} options, show all? (press any key and enter to accept): ")
        if show: print("All:", ', '.join(w))
        else:
            guess = input(f"Do you want suggestions, how many?\n(press any key and enter to accept/number to select amount): ")
            if guess:
                v = input("Be verbose? (press any key and enter to accept): ")
                if guess.isnumeric(): best_guess(w, int(guess), v)
                else: best_guess(w, 10, v)
        found = input("Game over? (press any key and enter to accept): ")

if __name__ == "__main__":
    solver()