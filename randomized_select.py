import random

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot
    pivot = random.choice(arr)

    # Partition the array into three parts
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return randomized_select(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return randomized_select(high, k - len(low) - len(equal))
