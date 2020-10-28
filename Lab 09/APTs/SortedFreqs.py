def freqs(data):
    """
    return list of int values corresponding
    to frequencies of strings in data, a list
    of strings
    """
    sorted_set = sorted(set(data))
    lst = []
    for word in sorted_set:
        occur = data.count(word)
        lst.append(occur)
    return lst

if __name__ == "__main__":
    print(freqs(["apple", "pear", "cherry", "apple", "cherry", "pear", "apple", "banana"]))
        
    
