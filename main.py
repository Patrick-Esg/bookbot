from stats import get_word_count, get_char_count , list_dictionary , sorter

#returns the contents of a text file with the path of file
#input String path_of_file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    frankenstein_text = get_book_text("/home/pat/workspace/github.com/Patrick-Esg/bookbot/books/frankenstein.txt")
    char_count_dict = get_char_count(frankenstein_text)
    list_dict = list_dictionary(char_count_dict)
   
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")    
    print("Found", get_word_count(frankenstein_text), "total words")
    print("--------- Character Count -------")

    for dic in sorter(char_count_dict):
        print(f"{dic["char"]}: {dic["num"]}")

    print("============= END ===============")

main()
