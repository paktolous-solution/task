

def algo(array, n):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x = array[i]**2
                y = array[j]**2
                z = array[k]**2
                if x == y+z or y == x+z or z == x+y:
                    return True
    return False


# It's time complexity will be O(n^3) where O is the size of array
# 
# 
array = [3, 1, 4, 6, 5]
if(algo(array, len(array))):
    print("Yes")
else:
    print("No")