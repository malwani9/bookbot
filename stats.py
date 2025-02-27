def get_number_of_words(book_content):
    words = book_content.split()
    return len(words)

def count_character_occurance(book_content):
    book_string = book_content.lower()
    characters_dict = {}
    for i in range(len(book_string)):
        if book_string[i] not in characters_dict:
            count = book_string.count(book_string[i])
            characters_dict[book_string[i]] = count   
    return characters_dict

def sort_dict(dictionary):
    dict_list = [{k: v} for k, v in dictionary.items()]
    dict_list.sort(reverse=True, key=lambda d: list(d.values())[0])
    return dict_list