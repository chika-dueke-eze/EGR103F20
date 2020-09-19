def falling(time,velo):
    g = 9.8
    dist = velo*time + 0.5*g*time**2
    return dist
    
    
if __name__ == "__main__":
    print(falling(3,5))
