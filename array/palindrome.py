def is_palindrome(string_to_test):
    i = 0
    j = len(string_to_test) - 1 

    while i <= j:
        if string_to_test[i] == string_to_test[j]:
            i += 1
            j -= 1
            continue
        else:
            return "not a palindrome"
    return "it's a palindrome"

def is_palindrome_python(string_to_test):
    if string_to_test == string_to_test[::-1]:
        return "is a palindrome"
    else:
        return "not a palindrome" 


if __name__ == "__main__":
    string_to_test = 'madam'

    print(is_palindrome_python(string_to_test))
