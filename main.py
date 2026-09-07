from stats import get_num_words, num_each_char, chars_dict_to_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents


def main():
    if len(sys.argv) > 1:
        bookfile = sys.argv[1]
    else:
        bookfile = "books/frankenstein.txt"

    booktext = get_book_text(bookfile)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}...")

    num_words = get_num_words(booktext)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_map = num_each_char(booktext)
    sorted_chars_list = chars_dict_to_sorted_list(char_map)

    print("--------- Character Count -------")
    print(sorted_chars_list)

    print("============= END ===============")


main()