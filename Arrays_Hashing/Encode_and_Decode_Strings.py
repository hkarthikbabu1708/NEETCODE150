# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

def encode(inp):
    res = ""
    for i in inp:
        res += str(len(i)) + "#" + i
    return res

def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = s.find("#", i)
        length = int(s[i:j])
        i = j + 1
        word = s[i: i + length]
        res.append(word)
        i = i + length
    return res

# inp = ["neet", "code", "love", "you"]
inp = ["we","say",":","yes"]
enc_str = encode(inp)
print(enc_str)
print(decode(enc_str))