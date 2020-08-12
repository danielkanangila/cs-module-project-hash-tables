# Your code here
from word_count import word_count


def histogram(filename):
    f = open(filename, "r")
    w_count = word_count(f.read())
    w_count = {k: v for k, v in sorted(
        w_count.items(), key=lambda item: item[1], reverse=True)}
    max_space = get_longest_word_n(w_count)
    for key, value in w_count.items():
        y = key
        x = ""
        times = value
        while(times > 0):
            x += "#"
            times -= 1
        print(print_y(y, max_space)+x)


def get_longest_word_n(w_dict):
    m = 0
    for item in w_dict.items():
        l = len(item[0])
        m = max(m, l)
    return m


def print_y(y_label, max_space_n):
    l_len = len(y_label)
    n_spaces = (max_space_n - l_len) + 2
    return y_label+n_spaces*' '


if __name__ == "__main__":
    histogram("robin.txt")
