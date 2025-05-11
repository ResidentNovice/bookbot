import sys

def chars_dict_to_sorted_list(chars):
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars_dict(text)
    dict_sorted = chars_dict_to_sorted_list(chars)
    print(f"{num_words} words found in the document")
    print(chars)
    print(dict_sorted)

main()