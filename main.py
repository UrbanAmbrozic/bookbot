def dict_to_list(chars_dict_sample):
    sorted = []

    for x in chars_dict_sample:
        sorted.append({"char": x , "num": chars_dict_sample[x]})
    
    sorted.sort(reverse=True, key=sort_on)

    return sorted

def sort_on(dict):
    return dict["num"]


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
    chars_dict_sorted = dict_to_list(chars_dict)

    num_words = get_num_words(text)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_dict_sorted:
        if item["char"].isalpha():
        
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
    
    

main()