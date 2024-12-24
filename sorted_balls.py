def sorted_balls(arr):
    low, mid, high = 0, 0, (len(arr)-1)


    while low <= high:
        
        if (arr[low] <= arr[mid] == "B"):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1 
            mid += 1 

        elif (arr[mid] == "G"):
            mid += 1 
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1 
    return sorted(arr)


array = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
print(sorted_balls(array))