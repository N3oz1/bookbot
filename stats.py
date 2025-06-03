def split_text(book_string):
    num_words = 0
    for i in range(len(book_string.split())):
        num_words += 1
    return print(f"{num_words} words found in the document")

def character_counter(book_string):
    dictionarie = {}
    lower_string = book_string.lower()
    for char in lower_string:
        if char in dictionarie:
            dictionarie[char] += 1
        else:
            dictionarie[char] = 1
    return dictionarie
        
    