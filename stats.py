#input is the string of text and returns the number of words in the string
def get_word_count(text):
    word_count = len(text.split())
    return word_count


def get_char_count(text):
    character_dict = {}

    for character in text:
        if character.lower() not in character_dict:
            character_dict[character.lower()] = 1
        else:
            character_dict[character.lower()] += 1

    return character_dict


def list_dictionary(dictionary):
    char_list = []

    for char in dictionary:
        curr_dict = {} #ditionary to append to list
        curr_dict["char"] = char
        curr_dict["num"] = dictionary[char]
        char_list.append(curr_dict)
    
    return char_list

def sort_list_dictionary(dict):
    return dict["num"]

def sorter(dictionary):
    chars_list = list_dictionary(dictionary)
    chars_list.sort(reverse=True, key=sort_list_dictionary)
    return chars_list 

