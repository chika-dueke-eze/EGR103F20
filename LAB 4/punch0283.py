'''
script that takes an integer and returns the sum of individual digits until it returns an int value less than 10
e.g. if we want to calculate the digit sum of 898, 8+9+8=25, but 25 is not less than 10 so we go on to add the 
individual values of 25, 2+5=7, since 7 < 10 we return 7 as the final value. This uses a recursive algorithm
'''

def digit_sum(x):
    while True:
        if len(str(x))== 1:      #base case
            return x
            break
        else:
            last_digit = x%10    #modulo command to find the last digit of an integer
            remaining_digits = x//10    #use to 'isolate' te remaining values after last digit has been gotten
            dsum = last_digit + digit_sum(remaining_digits)
            if len(str(dsum)) == 1:        #returns digit sum if the length of int is 1 (i.e. int < 10) 
                return dsum
            else:                           #if digit sum isn't less than 10 the function continues running until value less than 10 is reached
                last_digit = dsum%10
                remaining_digits = dsum//10
                dsum = last_digit + digit_sum(remaining_digits)
                return dsum

    
if __name__ == "__main__":
    print(digit_sum(999999999999))
