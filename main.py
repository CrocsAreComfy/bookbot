from stats import get_word_count
from stats import get_number_of_letters
from stats import sort_item
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    #book_text = get_book_text('books/frankenstein.txt')
    if (len(sys.argv)!= 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    wordCount = get_word_count(book_text)
    numberOfLetters = get_number_of_letters(book_text)
    sortedItem = sort_item(numberOfLetters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for char_dict in sortedItem:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")

main()