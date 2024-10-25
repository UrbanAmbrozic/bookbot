def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars
                

def get_num_words(text):
    string = text.split()
    return len(string)
    

def get_book_txt(path):
    with open(path) as file:
        return file.read()
 
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_txt(path)
    chars_dict = get_chars_dict(text)

    num_words = get_num_words(text)

    print(chars_dict)
    #print(f"There are {num_words} words in this document.")

main()