from stats import get_num_words
from stats import get_num_characters

def get_book_text(path: str) -> str:
    with open(path) as f:
        contents = f.read()
        return contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    character_count = get_num_characters(book_text)
    print(f"{word_count} words found in the document")
    print(character_count)


main()