import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


from stats import word_counter

from stats import char_counter

from stats import organize_char_count

def main():
    book_text = get_book_text(book_path)
    word_count = word_counter(book_text)
    char_count = char_counter(book_text)
    sorted_char_counts = organize_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_char_counts)):
        if sorted_char_counts[i]["char"].isalpha():
            print(f"{sorted_char_counts[i]['char']}: {sorted_char_counts[i]['num']}")
    print("============= END ===============")

main()
