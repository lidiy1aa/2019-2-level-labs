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
        if isinstance(word, str) and word not in self.storage:
            self.storage[word] = len(self.storage)
            return self.storage[word]
        return -1

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage.get(word)
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
            for elem in corpus:
                self.put(elem)
            return self.storage


class NGramTrie:
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple):
            new_sent = list(sentence)
            for i, n in enumerate(new_sent[:-self.size + 1]):
                n_gram = []
                counter = 0
                while counter < self.size:
                    n_gram.append(new_sent[i + counter])
                    counter += 1
                n_gram = tuple(n_gram)
                if n_gram in self.gram_frequencies.keys():
                    self.gram_frequencies[n_gram] += 1
                else:
                    self.gram_frequencies[n_gram] = 1
            return 'OK'
        else:
            return 'Error'

    def calculate_log_probabilities(self):
        my_dict = {}
        for trie_gram, freq in self.gram_frequencies.items():
            if trie_gram[:self.size - 1] not in my_dict:
                my_dict[trie_gram[:self.size - 1]] = freq
            else:
                my_dict[trie_gram[:self.size - 1]] += freq
        for trie_gram, freq in self.gram_frequencies.items():
            if trie_gram not in self.gram_log_probabilities:
                res = freq / my_dict[trie_gram[:self.size - 1]]
                self.gram_log_probabilities[trie_gram] = math.log(res)
        #return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        word_1 = []
        if not isinstance(prefix, tuple) or len(prefix) + 1 != self.size:
            return []
        final = list(prefix)
        while True:
            prob = []
            for n_gram in list(self.gram_log_probabilities.keys()):
                if n_gram[:-1] == prefix:
                    prob.append(self.gram_log_probabilities[n_gram])
            if not prob:
                break
            prob.sort(reverse=True)
            prob = prob[0]
            for word, probability in list(self.gram_log_probabilities.items()):
                if prob == probability:
                    word_1 = word[-1]
            final.append(word_1)
            pref_1 = list(prefix[1:])
            pref_1.append(word_1)
            prefix = tuple(pref_1)
        return final


def encode(storage_instance, corpus) -> list:
    code = []
    for sentence in corpus:
        code1 = []
        for element in sentence:
            element = storage_instance.get_id_of(element)
            code1.append(element)
        code.append(code1)
    return code


def split_by_sentence(text: str) -> list:
    prohibited_marks = (",", "#", "$", "\n", "@", "%", "^", "&", "*", "(", "'")
    new = ''
    if isinstance(text, str) and text is not None and len(text) > 1 and len(text.split()) > 1:
        for letter in text:
            if letter not in prohibited_marks and letter != '!' and letter != '?':
                new += letter
            elif letter in ('!', '?'):
                new += '.'
        split_1 = new.split()
        final = ' '.join(split_1)
        edit_text = []
        s_first = '<s>'
        s_last = '</s>'
        new_splitted = final.split('. ')
        for i, element in enumerate(new_splitted):
            if element[0].isupper():
                sth = ''
                sth += element.lower()
                edit_text.append(sth.split())
            elif element[0].islower():
                sth = ''
                sth += element.lower()
                if i > 0:
                    length = len(edit_text)
                    edit_text[length - 1].extend(sth.split())
        for i, element in enumerate(edit_text):
            element.insert(0, s_first)
            element.append(s_last)
        if edit_text[-1][-2]:
            edit_text[-1][-2] = edit_text[-1][-2][:-1]
        return edit_text
    return []


WSt = WordStorage()
NGr = NGramTrie(5)
sentences = split_by_sentence(REFERENCE_TEXT)
for sent in sentences:
    for word_ in sent:
        WSt.put(word_)
sentences1 = encode(WSt, sentences)
for sent in sentences1:
    NGr.fill_from_sentence(tuple(sent))
NGr.calculate_log_probabilities()
prefix1 = 'But as soon as'
pref_lst = prefix1.split()
pref_num = []
for pref in pref_lst:
    pref_num.append(WSt.get_id_of(pref))
print(pref_num)
numbers_res = NGr.predict_next_sentence(tuple(pref_num))
fin = []
for number in numbers_res:
    fin.append(WSt.get_original_by(number))
print(fin)
