def acronym(phrase):
    
    """
    phrase is a string, zero or more spaces
    return a string: acronym of the string 
    parameter phrase
    """
    word = phrase.split()
    acronym = ""
    for i in word:
        acronym = acronym + i[0]
    return acronym

if __name__ == '__main__':
    print(acronym("Self Contained Underwater Breathing Apparatus"))
