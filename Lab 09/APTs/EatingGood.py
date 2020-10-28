"""
link to pset: https://www2.cs.duke.edu/csed/pythonapt/eatinggood.html
"""

def howMany(meals, restaurant):
    meal_set = set(meals)
    count = 0
    for k in meal_set:
        info = k.split(":")
        name = info[0]
        eatery = info[1]
        if eatery == restaurant:
            count += 1
    return count

if __name__ == "__main__":
    print(howMany(['Sue:Elmos', 'Joe:Mad Hatter', 'Sue:Mad Hatter'], "Mad Hatter"))
