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
    return item["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for key, value in chars_dict.items():
        sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
