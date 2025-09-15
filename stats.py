def get_num_words(content: str) -> int:
    """Return the number of words in a given string."""
    words = content.split()
    return len(words)

def get_num_characters(content: str) -> dict:
    """Return a dictionary of each character that appears in a string."""
    word_list = content.split()
    character_counts = {}

    for word in word_list:
        for char in word:
            char = char.lower()
            if char not in character_counts:
                character_counts[char] = 1
            else:
                character_counts[char] += 1
    return character_counts

def __sort_on(items: dict) -> int:
    """Return value of item in dict to use in sorting."""
    return items["num"]

def get_sorted_list(items: dict) -> list:
    """Return a sorted dictionary in a list"""
    sorted_list = []
    for key in items:
        sorted_list.append({"char": key, "num": items[key]})
    sorted_list.sort(reverse=True, key=__sort_on)
    return sorted_list