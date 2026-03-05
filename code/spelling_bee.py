import os
import sys


def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    return set(word) <= set(letters)


def must_use(word, center):
    """Does word include the center letter?"""
    return center in word


def find_words(word_list, letters, center):
    """Find all valid words from a word list.

    - word_list: iterable of words (strings)
    - letters: string of allowed letters (7 letters)
    - center: single center letter that must appear
    """
    letters = letters.lower()
    center = center.lower()
    letters_set = set(letters)
    results = []
    for raw in word_list:
        w = raw.strip().lower()
        if len(w) < 4:
            continue
        if not w.isalpha():
            continue
        if not letters_set.issuperset(set(w)):
            continue
        if center not in w:
            continue
        results.append(w)
    return sorted(results)


def main():
    # get letters and center from argv or prompt
    if len(sys.argv) >= 3:
        letters = sys.argv[1].lower()
        center = sys.argv[2].lower()
    else:
        letters = input('Enter 7 letters (no spaces), e.g. abcdefg: ').strip().lower()
        center = input('Enter the center letter: ').strip().lower()

    if len(letters) != 7 or len(center) != 1 or center not in letters:
        print('Error: provide 7 letters and a center letter contained in them.')
        return

    # load words.txt relative to this file
    words_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'words.txt')
    try:
        with open(words_path, encoding='utf-8') as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print(f'words.txt not found at {words_path}')
        return

    found = find_words(words, letters, center)
    pangrams = [w for w in found if set(w) >= set(letters)]

    print(f'Found {len(found)} words. {len(pangrams)} pangram(s).')
    if pangrams:
        print('Pangrams:')
        for p in pangrams:
            print(' -', p)

    print('\nWords:')
    for w in found:
        print(w)


if __name__ == '__main__':
    main()
    
