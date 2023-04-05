def check_3_sum(num_array, target):
    num_array.sort()
    
    if len(num_array) < 3:
        return False

    for i in range(0, len(num_array) - 2):
        low = i + 1
        high = len(num_array) - 1
        check_sum = target - num_array[i]
        while low < high:
            if num_array[low] + num_array[high] == check_sum:
                return True
            elif num_array[low] + num_array[high] < check_sum:
                low += 1
            else:
                high -= 1

    return False
