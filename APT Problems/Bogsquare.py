def score(word):
    word_length = len(word)
    return word_length**2

if __name__ == "__main__":
    print(score("dog"))