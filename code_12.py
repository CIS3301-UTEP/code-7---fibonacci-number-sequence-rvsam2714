def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1 
    return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)


def get_fibonacci_number_sequence(number):
    if number == 0:
        return [0]
    if number == 1:
        return [0,1]
    start_sequence = [0,1]
    first = get_fibonacci_number(0)
    second = get_fibonacci_number(1)
    for i in range(2, number+1):
        current = first + second
        first = second
        second = current
        start_sequence.append(current)
    return start_sequence


if __name__ == "__main__":
    print(get_fibonacci_number(7))
    print(get_fibonacci_number_sequence(7))