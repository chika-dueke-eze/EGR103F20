def ratio(dna):
    
    """
    return float that's the cg ratio of the 
    nucleotides in the string parameter dna
    """
    counts = 0
    for letter in dna:
        if letter == 'c' or letter == 'g':
            counts += 1
    cg_ratio = counts/len(dna)
    return cg_ratio


if __name__ == '__main__':
    print(ratio('agatc'))
