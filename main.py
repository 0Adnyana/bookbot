import sys
from stats import get_num_words, get_char_count_dict, get_alpha_char_list

def get_book_text(filepath: str) -> str:
    with open(filepath) as bookFile:
        text = bookFile.read()
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookPath = sys.argv[1]
    bookText = get_book_text(bookPath)
    
    num_words = get_num_words(bookText)
    char_count = get_char_count_dict(bookText)
    char_list = get_alpha_char_list(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()