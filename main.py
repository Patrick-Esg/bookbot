from stats import get_word_count, get_char_count , list_dictionary , sorter
import sys

#returns the contents of a text file with the path of file
#input String path_of_file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    print(sys.argv)
    print("Usage: python3 main.py <path_to_book>")
    #frankenstein_text = get_book_text("/home/pat/workspace/github.com/Patrick-Esg/bookbot/books/frankenstein.txt")
    book_text = get_book_text(sys.argv[1])
    char_count_dict = get_char_count(book_text)
    list_dict = list_dictionary(char_count_dict)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")    
    print("Found", get_word_count(book_text), "total words")
    print("--------- Character Count -------")

    for dic in sorter(char_count_dict):
        print(f"{dic["char"]}: {dic["num"]}")

    print("============= END ===============")
    

main()
