def main():
    text = get_text("books/frankenstein.txt")
    print("-- Report from books/frankenstein.txt --")
    letter_dict = count_letter(text)
    num_word = count_word(text)
    print(f"{num_word} words found in the document")
    for letter in letter_dict:
        if letter.isalpha():
            print(f"{letter} was found {letter_dict[letter]} times.")
    print("--End report--")




def count_word(text):
    words = text.split()
    return len(words)

def get_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_letter(text):
    letter_dict = {}
    lowercase_text = text.lower()
    for letter in lowercase_text:
        if not letter in letter_dict: 
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1 
    return letter_dict
    
main()