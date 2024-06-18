# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, words):
        matches = []
        for candidate in words:
            if ''.join(sorted(candidate.lower())) == self.sorted_word:
                matches.append(candidate)
        return matches