def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Split array into sublists of 5, sort them, and find medians
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Find the median of the medians
    median = median_of_medians(medians, len(medians) // 2)

    # Partition the array into three parts
    low = [x for x in arr if x < median]
    high = [x for x in arr if x > median]
    equal = [x for x in arr if x == median]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return median
    else:
        return median_of_medians(high, k - len(low) - len(equal))