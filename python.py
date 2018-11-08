def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n - 1)
print("Hello world!\n")
print(factorielle(9))