from stats import get_num_words, num_each_char, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookfile = sys.argv[1]
    frank = get_book_text(bookfile)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}...")
    num_words = get_num_words(frank)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_map = num_each_char(frank)
    sorted_chars_list = chars_dict_to_sorted_list(char_map)
    print("--------- Character Count -------")
    for item in sorted_chars_list:
        char = item['char']
        count = item['num']

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
