
def reverse_list(list_to_revert):
    i = 0
    j = len(list_to_revert) - 1

    while i <= j:
        list_to_revert[i], list_to_revert[j] = list_to_revert[j], list_to_revert[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    list_to_revert = [1,2,3,4]

    print(list_to_revert)
    reverse_list(list_to_revert)
    print(list_to_revert)
