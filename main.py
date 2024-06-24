def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_count = get_num_letters(text)

    #Convert into a list of dictionaries.
    char_list = [{"char": char, "num": num} for char, num in char_count.items()]

    #Sort the list
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def sort_on(item):
    return item["num"]


def get_num_letters(text):
    lowered_text = text.lower()
    char_count = dict()

    for char in lowered_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count



def get_num_words(text):
    words = text.split()
    return len(words)

    
def get_book_text(path):
    with open(path) as f:
        return f.read()



main()