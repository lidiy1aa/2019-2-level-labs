from math import log


REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    prohibited_marks = (",", "#", "$", "\n", "@", "%", "^", "&", "*", "(", ")", "'", "/", ">", "-", ".", "?", "!")
    token_corpus = []
    if texts:
        for text_ in texts:
            if isinstance(text_, str):
                clean_text = ''
                while '<br' in text_:
                    text_ = text_.replace('<br', '')
                for letter in text_:
                    if letter not in prohibited_marks:
                        if letter.isupper():
                            clean_text += letter.lower()
                        elif letter.islower() or letter == ' ':
                            clean_text += letter
                text_split = clean_text.split()
                token_corpus.append(text_split)
    return token_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus:
            for text1 in self.corpus:
                tf = {}
                if text1:
                    text_length = len(text1)
                    for word in text1:
                        if not isinstance(word, str):
                            text_length -= 1
                    for word in text1:
                        if isinstance(word, str) and word not in tf:
                            word_count = text1.count(word)
                            tf[word] = word_count / text_length
                    self.tf_values.append(tf)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            texts_count = len(self.corpus)
            count_freq = {}
            for text1 in self.corpus:
                if not text1:
                    continue
                for word in text1:
                    if isinstance(word, str):
                        if word not in count_freq.keys():
                            word_in_text = 0
                            count_freq[word] = word_in_text
                            for text_again in self.corpus:
                                if not text_again or word in text_again:
                                    count_freq[word] += 1
                for word in count_freq.keys():
                    if count_freq.get(word) != 0:
                        self.idf_values[word] = log(texts_count / count_freq.get(word))
        return self.idf_values

    def calculate(self):
        if self.tf_values and self.idf_values:
            for text1 in self.tf_values:
                tf_idf_value = {}
                for word, tf in text1.items():
                    tf_idf_value[word] = tf * self.idf_values[word]
                self.tf_idf_values.append(tf_idf_value)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        try:
            val = self.tf_idf_values[document_index][word]
        except (TypeError, IndexError, KeyError):
            return ()
        tf_idf_sort = sorted(self.tf_idf_values[document_index].items(), key=lambda x: -x[1])
        rating = [array[0] for array in tf_idf_sort].index(word)
        return val, rating

    # scenario to check your work


test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))