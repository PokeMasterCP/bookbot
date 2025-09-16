from stats import *
import sys

def get_book_text(path: str) -> str:
    with open(path) as f:
        contents = f.read()
        return contents

def format_output(word_count: int, char_count: list, book: str) -> str:
    """Output formatted data based on input list."""
    output = "============ BOOKBOT ============"
    output += f"\nAnalyzing book found at {book}..."
    output += "\n---------- Word Count ----------"
    output += f"\nFound {word_count} total words"
    output += "\n--------- Character Count -------"
    
    for char in char_count:
        character = char["char"]
        num = char["num"]
        if character.isalpha():
            line = f"\n{character}: {num}"
            output += line
    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file = sys.argv[1] 
    book_text = get_book_text(file)
    word_count = get_num_words(book_text)
    unsorted_char_count = get_num_characters(book_text)
    sorted_char_count = get_sorted_list(unsorted_char_count)
    
    output = format_output(word_count, sorted_char_count, file)
    print(output)

main()