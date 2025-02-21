def count_un_an_words(text):
    words = text.split()
    count = 0

    for word in words:
        if word.startswith("un") and word.endswith("an"):
            count += 1

    return count
text = "unbroken an unusual unhuman unkind an unknowan"
print(count_un_an_words(text))  # Output: 2 (unhuman, unknowan)
