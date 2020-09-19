def geo_prog(a, s, r):
    try:
        a = float(a)
        s = float(s)
        r = float(r)
        
        if a<= 0 or s<=0 or r<=0:
            print("All arguments must be positive")
            return -2,-2
        
        lst = []
        if 0<r<1:
            if a*r < s:
                print('Invalid sequence')
                return -3,-3
            n = 0
            while True:
                terms = a*(r**(n))
                n += 1
                if terms >= s:
                    lst.append(terms)
                    continue
                else:
                    count= 0
                    for x in lst:
                        count = count + x
                    return lst, count
                
        if r == 1:
            lst.append(a)
            return lst, a
            
        if r>1:
            if a*r > s:
                print('Invalid sequence')
                return -3,-3
            n = 0
            while True:
                terms = a*(r**(n))
                n += 1
                if terms <= s:
                    lst.append(terms)
                    continue
                else:
                    count= 0
                    for x in lst:
                        count = count + x
                    return lst, count

    except:
        print('All arguments must be single numbers')
        return -1,-1

if __name__ == "__main__":
    print(geo_prog(20,1,0.3))
