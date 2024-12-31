with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def word_count(file_contents):
    words = file_contents.split()
    word_number = len(words)
    print(word_number)

def char_count(file_contents):
    count = {}
    lowercase = file_contents.lower()
    for char in lowercase:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    print(count)
char_count(file_contents)