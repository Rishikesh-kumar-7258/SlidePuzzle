def Pivot_sort(arr):

    if (len(arr) < 2) : return arr

    pivot = arr[0]

    left = []
    right = []

    for a in arr:
        if a.y > pivot.y : right.append(a)
        elif a.y < pivot.y : left.append(a)
        else : 
            if a.x > pivot.x : right.append(a)
            elif a.x < pivot.x : left.append(a)
    
    left = Pivot_sort(left)
    right = Pivot_sort(right)

    left.append(pivot)
    left.extend(right)
    
    return left