def bagelCount(orders):
    """
    return number of bagels needed to fulfill
    the orders in integer list parameter orders
    """
    counts = 0
    for bagels in orders:
        extra_bagels = bagels // 12
        counts += bagels + extra_bagels
    return counts

if __name__ == "__main__":
    print(bagelCount([11,22,33,44,55]))
        
    
