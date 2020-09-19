import math

def volume(radius, height):
    vol = 1/3 * math.pi * radius**2 * height
    return vol

if __name__ == "__main__":
    print(volume(1,1))
    print(volume(10,10))
    