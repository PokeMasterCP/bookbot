from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list

def get_book_text(path: str) -> str:
    with open(path) as f:
        contents = f.read()
        return contents
def format_output(word_count: int, char_count: list) -> str:
    """Output formatted data based on input list."""
    output = "============ BOOKBOT ============"
    output += "\nAnalyzing book found at books/frankenstein.txt..."
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
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    unsorted_char_count = get_num_characters(book_text)
    sorted_char_count = get_sorted_list(unsorted_char_count)
    
    output = format_output(word_count, sorted_char_count)
    print(output)

main()