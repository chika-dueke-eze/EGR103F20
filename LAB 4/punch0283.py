def digit_sum(x):
    while True:
        if len(str(x))== 1:
            return x
            break
        
        else:
            last_digit = x%10
            remaining_digits = x//10
            dsum = last_digit + digit_sum(remaining_digits)

        if len(str(dsum)) == 1:
            return dsum
        else:
            last_digit = dsum%10
            remaining_digits = dsum//10
            dsum = last_digit + digit_sum(remaining_digits)
            return dsum

    

print(digit_sum(98766))
