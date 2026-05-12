def print_chars(chars, index=0):
    if index == len(chars):
        return
    print(chars[index], end='')
    print_chars(chars, index + 1)

hello = list("Hello, World!")
print(hello)         # show as array
print_chars(hello)   # print recursively
print()              # newline
