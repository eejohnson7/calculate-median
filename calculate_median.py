def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    
    return median

print(find_median([1,2,3,4,5, 6]))
