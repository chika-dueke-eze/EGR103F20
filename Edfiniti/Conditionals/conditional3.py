phrase = "the cow jumped over the moon"

count = 0
for letter in phrase:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print(count)
