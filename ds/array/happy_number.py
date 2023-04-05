
def happy_number(num):
    slow = sum_of_digits(num)
    fast = sum_of_digits(slow)

    return happy_num_helper(slow, fast)


def happy_num_helper(slow, fast):
    if fast == 1:
        return True
    elif fast == slow:
        return False
    else:
        slow = sum_of_digits(slow)
        fast = sum_of_digits(sum_of_digits(fast))

        return happy_num_helper(slow, fast)


def sum_of_digits(num):
    total_sum = 0
    while True:
        digit = num % 10
        num = num // 10
        total_sum = total_sum + pow(digit, 2)

        if num == 0:
            break
    return total_sum


if __name__ == "__main__":
    print(happy_number(8))


