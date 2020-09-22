def maxPoints(toss):  
    """
    return int representing the maximal Yahtzee
    score based on rolls in integer list toss
    """
    lst = []
    for num in toss:
        occurence = toss.count(num)       #gets the total no of times a value appears in the list
        total_num = num * occurence
        lst.append(total_num)
    lst.sort(reverse=True)
    print(lst)          #---------------> used this for debugging **disregard**
    highest_val = lst[0]
    return highest_val

if __name__ == "__main__":
    print(maxPoints([2,2,3,5,4]))
    
        
