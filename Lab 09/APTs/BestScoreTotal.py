def total(scores):
    count = 0
    for i in scores:
        lst = []
        val = i.split()
        for k in val:
            int_val = int(k)
            lst.append(int_val)
        max_val = max(lst)
        count += max_val
    return count

if __name__ == "__main__":
    print(total(['10 3 8 7 7 8 4 0 8 0', '6 10', '9', '5 3 5 1 3 9 3 3']))
        
        
