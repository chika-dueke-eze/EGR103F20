def networth(transactions):
    d = {}
    lst = []
    for k in range(len(transactions)):
        info = transactions[k].split(":")
        sender = info[0]
        receiver = info[1]
        amount = float(info[2])*100
        d[sender] = d.get(sender, 0) - amount
        d[receiver] = d.get(receiver, 0) + amount
    for name,netflow in d.items():
        name = str(name)
        netflow /= 100
        netflow = str(netflow)
        val = name+':'+netflow
        lst.append(val)
        lst.sort()
    return lst
        
if __name__ == "__main__":
    print(networth(["owen:susan:10", "owen:robert:10", "owen:drew:10"]))
    print(networth( ['fred:ricky:50', 'ricky:fred:20', 'fred:ethel:100', 'ethel:fred:150.35']))
