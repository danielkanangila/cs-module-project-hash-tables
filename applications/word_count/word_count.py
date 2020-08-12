def word_count(s):
    # Your code here
    wList = s.split()
    ignored_char = [":", ";", ",", ".", "-", "+", "=", "/", "\\",
                    " | ", "[", "]", "{", "}", "(", ")", "*", " ^ ", " &", ]

    d = {}

    for word in wList:
        if word in ignored_char:
            continue
        word = parse(word.lower())
        if word != "":
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d


def parse(s):
    w = ""
    for char in s:
        if char == "'":
            w += char
        if char.isalnum():
            w += char
    return w


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
