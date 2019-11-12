import csv


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if isinstance(num_rows, int) is True and isinstance(num_cols, int) is True:
        edit_matrix = [[0] * num_cols for i in range(num_rows)]
    else:
        edit_matrix = []
    return edit_matrix


def initialize_edit_matrix(edit_matrix, add_weight, remove_weight):
    new_edit = list(edit_matrix)
    if new_edit is None or not new_edit or not new_edit[0]:
        return new_edit
    if isinstance(add_weight, int) and isinstance(remove_weight, int):
        new_edit[0][0] = 0
        for i in range(0, len(new_edit)):
            if i != 0:
                new_edit[i][0] = new_edit[i - 1][0] + remove_weight
            for j in range(len(new_edit[0])):
                if j != 0:
                    new_edit[0][j] = new_edit[0][j - 1] + add_weight
    return new_edit


def minimum_value(numbers):
    value = (min(numbers))
    return value


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str):
    new_edit = list(edit_matrix)
    if new_edit:
        if isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int) and\
                original_word and target_word:
            for i in range(1, len(new_edit)):
                for j in range(1, len(new_edit[i])):
                    var1 = new_edit[i - 1][j] + remove_weight
                    var2 = new_edit[i][j - 1] + add_weight
                    if original_word[i - 1] != target_word[j - 1]:
                        var3 = new_edit[i - 1][j - 1] + substitute_weight
                    else:
                        var3 = new_edit[i - 1][j - 1]
                    value = (var1, var2, var3)
                    new_edit[i][j] = minimum_value(value)
    return new_edit


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if isinstance(original_word, str) is True and isinstance(target_word, str) is True and \
        isinstance(remove_weight, int) is True and \
            isinstance(substitute_weight, int) is True and isinstance(add_weight, int) is True:
        num_cols, num_rows = len(original_word) + 1, len(target_word) + 1
        new_edit = tuple(initialize_edit_matrix(tuple(generate_edit_matrix(num_cols, num_rows)), add_weight,
                                                remove_weight))
        final_matrix = fill_edit_matrix(new_edit, add_weight, remove_weight, substitute_weight, original_word,
                                        target_word)
        print(final_matrix[-1][-1])
        return final_matrix[-1][-1]
    return -1


def save_to_csv(edit_matrix, path_to_file: str):
    with open(path_to_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(edit_matrix)


def load_from_csv(path_to_file: str):
    matrix = []
    with open(path_to_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    return list(row)
