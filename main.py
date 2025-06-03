from stats import split_text
from stats import character_counter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents

def main():
    string = get_book_text("/home/paulius-puzinkevicius/boot/bookbot/books/frankenstein.txt")
    split_text(string)
    symbol_count = character_counter(string)
    print(symbol_count)

main()
