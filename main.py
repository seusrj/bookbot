from stats import get_num_words, get_character_number, sort_dict_by_wordnumber
import sys

def get_book_text(file_name: str):
    with open(file_name, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    d:dict = get_character_number(file_contents)
    l:list = sort_dict_by_wordnumber(d)
    for item in l:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()