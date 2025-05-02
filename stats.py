def word_counter(book_text):
    words = book_text.split(sep=None, maxsplit=-1)
    return len(words)

def char_counter(book_text):
    characters = {}
    for char in book_text:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters

def organize_char_count(char_count_dict):
    sorted_chars_dict_list = [{"char": char, "num": count} for char, count in char_count_dict.items()]
    sorted_chars_dict_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars_dict_list
