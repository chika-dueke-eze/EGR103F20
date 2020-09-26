def decrypt(library,message):
    """
    return String for parameters
    library a list of Strings
    and message a string
    """
    dictcode = {}
    for e in library:
        code = e.split()
        dictcode[code[1]] = code[0]      #map the codes to letters with a dictionary
        
    decoded = ""
    split_msg = message.split()              #split the code
    for msg in split_msg:
        decoded += dictcode.get(msg, "?") + ""      #get code from dict
    return decoded
    
if __name__ == "__main__":
    print(decrypt([
 "H -.-.-.-.-.-.-.-.-.-.",
 "I .-.-.-.-.-.-.-.-.-.-",
 "K -.-.-.-.-.",
 "E .-.-.-.-.-"],"-.-.-.-.-.-.-.-.-.-. .-.-.-.-.-.-.-.-.-.-"))
    
    
    
        
        
