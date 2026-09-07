def get_num_words(booktext):
    words = booktext.split()
    return len(words)

def num_each_char(booktext):
    each_char = {}
    for char in booktext:
        lowercase_char = char.lower()
        if lowercase_char in each_char:
            each_char[lowercase_char] += 1
        else:
            each_char[lowercase_char] = 1
    return each_char

def sort_on(item):
    return item[1]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for char in chars_dict:
        count = chars_dict[char]
        sorted_list.append((char, count))

    sorted_list = sorted(
        sorted_list,
        key=sort_on,
        reverse=True
    )

    return sorted_list
