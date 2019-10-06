"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def read_from_file(path_to_file, lines_limit):
    doc = open(path_to_file, 'r')
    test = ''
    lines_limit = 7
    for i, line in enumerate(doc):
        if i < lines_limit:
            test += line
        else:
            break
    return test
    doc.close()


def calculate_frequences(text):
    prohibited_marks = (',', '.', '\n', ':', ';', '#', '@', '$', '^', '&', '*', '%', '~', '"', '\'')
    if text is None:
        print('None given')
        freq_dict = {}
        return freq_dict
    else:
        if type(text) is int:
            print('The text is integer')
            freq_dict = {}
            return freq_dict
        elif len(text) == 0:
            print('The text is empty')
            freq_dict = {}
            return freq_dict
        else:
            freq_dict = {}
            low_text = text.lower()
            text_split = low_text.split()
            res = []
            for word in text_split:
                if not word.isdigit() and word not in prohibited_marks:
                    clear_word = ''
                    for c in word:
                        if c not in prohibited_marks and not c.isdigit():
                            clear_word += c
                    if clear_word is not '':
                        res.append(clear_word)
            for word in res:
                count = freq_dict.get(word, 0)
                freq_dict[word] = count + 1
            frequency_list = freq_dict.keys()
            for words in frequency_list:
                print(words, freq_dict[words])
    return freq_dict
    """
    Calculates number of times each word appears in the text
    """
    pass


def filter_stop_words(freq_dict, stop_words):
    if stop_words is None or freq_dict is None or len(freq_dict) == 0:
        print('Error')
        new_frequency = {}
        return new_frequency
    elif len(stop_words) == 0:
        print(freq_dict)
        return freq_dict
    else:
        new_frequency = freq_dict.copy()
        for stop_word in stop_words:
            if isinstance(stop_word, str) and len(stop_word) > 0:
                if new_frequency.get(stop_word):
                    new_frequency.pop(stop_word)
        for key in new_frequency.keys():
            if key in stop_words or isinstance(key, int):
                new_frequency.pop(key)
                print(new_frequency)
                return new_frequency
    return new_frequency

    """
    Removes all stop words from the given frequencies dictionary
    """
    pass


def get_top_n(new_frequency, top_n):
    if new_frequency == {} or top_n <= 0:
        return ()
    else:
        sorted_list = sorted(new_frequency.items(), key=lambda i: i[1], reverse=True)
        final = []
        final = [element[0] for element in sorted_list]
        if top_n > len(final):
            return tuple(final)
        elif len(final) >= top_n:
            final_top = final[:top_n]
            print(tuple(final_top))
            return tuple(final_top)

    """
    Takes first N popular words
    """
    pass


def write_to_file(path_to_file, content):
    doc = open(path_to_file, 'w')
    for word in content:
        doc.write(word + '\n')
    doc.close()
