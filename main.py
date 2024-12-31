with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def word_count(file_contents):
    words = file_contents.split()
    word_number = len(words)
    return(word_number)

def char_count(file_contents):
    count = {}
    lowercase = file_contents.lower()
    for char in lowercase:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return(count)

def book_report(word_number, count):
    filtered_count = {}
    for key, value in count.items():
        if key.isalpha():
            filtered_count[key] = value
    filtered_list = list(filtered_count.items())
    sorted_list = sorted(filtered_list, key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_number} words found in the document\n")
    for char, num in sorted_list:
        print(f"The '{char}' charcter was found {num} times")
    print("--- End Report ---")

word_number = word_count(file_contents)
character_count = char_count(file_contents)
book_report(word_number, character_count)