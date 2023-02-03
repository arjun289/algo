def valid_palindrome(s):
    low = 0
    high = len(s) - 1
    error = 0

    while low <= high:
        if s[low] == s[high] and error <= 1:
            low += 1
            high -= 1
            continue
        elif s[low+1] == s[high] and error < 1:
            low += 2
            high -= 1
            error += 1
            continue
        elif s[low] == s[high-1] and error < 1:
            low += 1
            high -= 2
            error += 1
            continue
        else:
            return False

    return True
