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
    

if __name__ == "__main__":
    print(get_fibonacci_number(4))