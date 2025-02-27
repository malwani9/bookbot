from stats import get_number_of_words
from stats import count_character_occurance
from stats import sort_dict
def get_book_text(book_file):
    with open(book_file, 'r') as f:
        book_content = f.read()
    return book_content

def main():
    book_string = get_book_text('books/frankenstein.txt')
    num_words = get_number_of_words(book_string)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters_occurrances_dict = count_character_occurance(book_string)
    sorted_list_dict = sort_dict(characters_occurrances_dict)
    for item in sorted_list_dict:
        for key in item:
            if (key.isalpha()):
                print(f"{key}: {item[key]}")
    print("============= END ===============")
main()
