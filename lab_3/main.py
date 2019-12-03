"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        a = 0
        if isinstance(word, str) and word not in self.storage:
            if word not in self.storage:
                self.storage[word] = a
        return self.storage.get(word)

    def get_id_of(self, word: str) -> int:
        if isinstance(word, str):
            for key, value in self.storage.items():
                if key == word:
                    return value
            else:
                return -1
        else:
            return -1

    def get_original_by(self, id1: int) -> str:
        if isinstance(id1, int):
            for key, value in self.storage.items():
                if value == id1:
                    return key
        else:
            return 'UNK'
        if id1 not in self.storage.values():
            return 'UNK'

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            count = 0
            for word in corpus:
                self.storage[word] = count
                count += 1
        else:
            return -1
        return corpus


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        # if self.size == 3:
        if isinstance(sentence, tuple):
            new_sent = list(sentence)
            keys_freq = []
            for i in range(len(new_sent) - 1):
                if i != len(new_sent) - (self.size - 1):
                    n_gram = []
                    counter = 0
                    while counter < self.size:
                        n_gram.append(new_sent[i + counter])
                        counter += 1
                    n_gram = tuple(n_gram)
                    keys_freq.append(n_gram)
                    print(n_gram)
            self.gram_frequencies = dict((n_gram, keys_freq.count(n_gram)) for n_gram in keys_freq)
            return 'OK'
        else:
            return 'Error'

    def calculate_log_probabilities(self):
        my_dict = {}
        for trie_gram, freq in self.gram_frequencies.items():
            if trie_gram[:-1] not in my_dict:
                my_dict[trie_gram[:-1]] = freq
            else:
                my_dict[trie_gram[:-1]] += freq
        for trie_gram, freq in self.gram_frequencies.items():
            res = freq / my_dict[trie_gram[:-1]]
            self.gram_log_probabilities[trie_gram] = math.log(res)
        print(self.gram_log_probabilities)
        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        self.gram_log_probabilities = {(1, 2): -0.18, (1, 3): -1.79, (2, 3): -1, (2, 4): -2, (3, 4): -0.1,
         (3, 5): -1.8}
        new_list = []
        if not isinstance(prefix, tuple) or len(prefix) + 1 != self.size:
            return []
        else:
            while True:
                final = list(prefix)
                for trie_gram in self.gram_log_probabilities.keys():
                    if trie_gram[:-1] == prefix:
                        new_list.append(self.gram_log_probabilities[trie_gram])
                if not new_list:
                    break
                else:
                    new_list = max(new_list)
                    for word, probability in self.gram_log_probabilities.items():
                        if new_list == probability:
                            final.append(word[-1])
                    print(final)
                    return final
                new_prefix = prefix[]
            return final


def encode(storage_instance, corpus) -> list:
    for sentence in corpus:
        for i, el in enumerate(sentence):
            for keyword, ind in storage_instance.items():
                if el == keyword:
                    sentence[i] = ind
    return corpus


def split_by_sentence(text: str) -> list:
    prohibited_marks = (",", "#", "$", "\n", "@", "%", "^", "&", "*", "(", "'")
    new = ''
    if isinstance(text, str) and text is not None and len(text) > 1 and len(text.split()) > 1:
        for letter in text:
            if letter not in prohibited_marks and letter != '!' and letter != '?':
                new += letter
            elif letter == '!' or letter == '?':
                new += '.'
        x = new.split()
        final = ' '.join(x)
        edit_text = []
        s_first = '<s>'
        s_last = '</s>'
        new_splitted = final.split('. ')
        for i, el in enumerate(new_splitted):
            if el[0].isupper():
                b = ''
                b += el.lower()
                edit_text.append(b.split())
            elif el[0].islower():
                b = ''
                b += el.lower()
                if i > 0:
                    length = len(edit_text)
                    edit_text[length - 1].extend(b.split())
        for i, el in enumerate(edit_text):
            el.insert(0, s_first)
            el.append(s_last)
        if edit_text[-1][-2]:
            edit_text[-1][-2] = edit_text[-1][-2][:-1]
        return edit_text
    return []


# corpus = split_by_sentence(str(f))
# s = WordStorage
# s.put()
# encode(corpus)
x = NGramTrie(2)
# x.fill_from_sentence()
# x.calculate_log_probabilities()
x.predict_next_sentence((1,))
