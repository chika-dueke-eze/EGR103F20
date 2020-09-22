import math
def minutesNeeded (numCakes, capacity):
    """
    return integer representing time to cook pancakes
    based on integer parameters as described below
    """
    shortest_time = math.ceil((numCakes)*2/capacity)* 5
    return shortest_time

if __name__ == "__main__":
    print(minutesNeeded (2, 3))
