x = int(input())
y = int(input())
z = int(input())

if x+y == 0:
    print ('zero sum found')
elif x+z == 0:
    print ('zero sum found')
elif y+z == 0:
    print ('zero sum found')
elif x+y+z == 0:
    print ('zero sum found')
else:    
    print('no zero sum found')
