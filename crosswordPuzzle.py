def can_place_h(crossword, word, r, c):
    if c + len(word) > 10:
        return False
    if c > 0 and crossword[r][c - 1] != '+':
        return False
    if c + len(word) < 10 and crossword[r][c + len(word)] != '+':
        return False
    for i in range(len(word)):
        if crossword[r][c + i] not in ('-', word[i]):
            return False
    return True


def can_place_v(crossword, word, r, c):
    if r + len(word) > 10:
        return False
    if r > 0 and crossword[r - 1][c] != '+':
        return False
    if r + len(word) < 10 and crossword[r + len(word)][c] != '+':
        return False
    for i in range(len(word)):
        if crossword[r + i][c] not in ('-', word[i]):
            return False
    return True


def place_h(crossword, word, r, c):
    changed = []
    for i in range(len(word)):
        if crossword[r][c + i] == '-':
            crossword[r][c + i] = word[i]
            changed.append((r, c + i))
    return changed


def place_v(crossword, word, r, c):
    changed = []
    for i in range(len(word)):
        if crossword[r + i][c] == '-':
            crossword[r + i][c] = word[i]
            changed.append((r + i, c))
    return changed


def remove_word(crossword, changed):
    for r, c in changed:
        crossword[r][c] = '-'


def solve(crossword, words, index):
    if index == len(words):
        return True

    word = words[index]

    for r in range(10):
        for c in range(10):
            if can_place_h(crossword, word, r, c):
                changed = place_h(crossword, word, r, c)
                if solve(crossword, words, index + 1):
                    return True
                remove_word(crossword, changed)

            if can_place_v(crossword, word, r, c):
                changed = place_v(crossword, word, r, c)
                if solve(crossword, words, index + 1):
                    return True
                remove_word(crossword, changed)

    return False


def crosswordPuzzle(crossword, words):
    words = words.split(";")
    crossword = [list(row) for row in crossword]
    solve(crossword, words, 0)
    return [''.join(row) for row in crossword]





    
