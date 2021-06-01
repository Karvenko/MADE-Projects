"""Task D solution"""

import sys

ALPHABET_START = ord('a')
ALPHABET_END = ord('z')
# ALPHABET_END = ord('c')
ALPHABET_LEN = ALPHABET_END - ALPHABET_START + 1
MAX_LEN = 30

class Node:
    def __init__(self):
        self.is_terminal = False
        self.next = [None] * ALPHABET_LEN

class Trie():
    def __init__(self):
        self.root = Node()

    def add(self, word):
        """Adds word to Trie"""
        p = self.root
        for c in word:
            idx = ord(c) - ALPHABET_START
            if not p.next[idx]:
                p.next[idx] = Node()
            p = p.next[idx]
        p.is_terminal = True
        return

    def get_all_words(self, string):
        """Returns set of all substrings of string which are in Trie"""
        result = set()
        p = self.root
        for l in range(len(string)):
            idx = ord(string[l]) - ALPHABET_START
            if not p.next[idx]:
                break
            p = p.next[idx]
            if p.is_terminal:
                result.add(string[:l + 1])
        return result

def is_in_text(ps, t):
    trie = Trie()
    word_set = set()
    result = []
    for word in ps:
        trie.add(word)
    for i in range(len(t)):
        word_set.update(trie.get_all_words(t[i:i + MAX_LEN]))
    for p in ps:
        if p in word_set:
            result.append('Yes')
        else:
            result.append('No')
    return result

if __name__ == '__main__':
    data = sys.stdin.readlines()
    data = [x.strip() for x in data]
    result = is_in_text(data[2:], data[0])
    sys.stdout.write('\n'.join(result))