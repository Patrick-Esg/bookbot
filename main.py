#returns the contents of a text file with the path of file
#input String path_of_file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

#input is the string of text and returns the number of words in the string
def get_word_count(text):
    word_count = len(text.split())
    return word_count

def main():
    frankenstein_text = get_book_text("/home/pat/workspace/github.com/Patrick-Esg/bookbot/books/frankenstein.txt")
    #print(frankenstein_text)
    print(get_word_count(frankenstein_text), "words found in the document")

main()
