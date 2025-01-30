def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    lowered_text = text.lower()
    character_count = get_character_count(lowered_text)
    character_count_sorted = sort_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for entry in character_count_sorted:
        if entry["char"].isalpha():
            print(f"The '{entry['char']}' character was found {entry['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open (path) as f:
        return f.read()

def get_word_count(full_text):
    words = full_text.split()
    return len(words)

def get_character_count(full_text):
    character_dict = {}
    for char in full_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(d):
    return d["num"]

def sort_list(chars):
    sorted_list = []
    for char in chars:
        sorted_list.append({"char": char, "num": chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
