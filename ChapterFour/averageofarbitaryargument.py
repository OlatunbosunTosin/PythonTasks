def average(number, *args):
    sum_of_argument = sum(args)
    length_of_argument = len(args)
    return (number + sum_of_argument) / (1 + length_of_argument)
