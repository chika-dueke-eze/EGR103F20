import math
def bags(strength, food):
    
    """
    return int based on parameters strength, an int
    and food a list of Strings
    """
    each_food = set(food)                   #gets unique elements of items in food list.
    count = 0
    for i in each_food:
        sum_each_food = food.count(i)
        bags_needed = math.ceil(sum_each_food/strength)     #returns the number of bags needed to pack groceries
        count = count + bags_needed
    return count

if __name__ == "__main__":                 #test
    print(bags(3,["DAIRY",
 "DAIRY",
 "PRODUCE",
 "PRODUCE",
 "PRODUCE",
 "MEAT"
]))
          
