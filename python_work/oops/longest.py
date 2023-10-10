def max_word(*args):
    return max(args,key=lambda w:len(w))

print(max_word("hello","jumana","jeza"))