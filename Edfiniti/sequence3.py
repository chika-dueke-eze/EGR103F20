weather = ["sunny", "cloudy", "partially sunny", "rainy", "storming", "foggy", "hailing"]

for word in weather:
    char = len(word)
    fc = word[0]
    lc = word[-1]
    
    print("The word is {} characters".format(char))
    print("The first character is: {}".format(fc))
    print("The last character is: {}".format(lc))
    
