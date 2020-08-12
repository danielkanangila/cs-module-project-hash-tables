# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


most_frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


# get substution key to build the decode table
def get_sub_key(s):
    # count the frequency of letters in cipher
    d = {}
    for char in s:
        if char.isalpha():
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

    # asc sort of the frequency dictionary
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    # reversed the most frequent letters list
    mf_reversed = most_frequent[::-1]
    # map the frequency dictionary build from cipher with the most frequent letters list
    decode_table = {}
    for i,  (k, v) in enumerate(d.items()):
        decode_table[k] = mf_reversed[i]
    return decode_table


def decode(cipher_text):
    decode_table = get_sub_key(cipher_text)
    plain_text = ''
    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else:
            if char in decode_table:
                plain_text += decode_table[char.upper()]
            else:
                plain_text += char
    return plain_text


if __name__ == "__main__":
    f = open("ciphertext.txt", "r")
    cipher = f.read()

    decoded_text = decode(cipher)
    print(decoded_text)
