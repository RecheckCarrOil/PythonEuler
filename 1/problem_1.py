# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def is_multiple_of_3(input_value):
    return input_value % 3 == 0 and input_value > 0


def is_multiple_of_5(input_value):
    return input_value % 5 == 0 and input_value > 0


def sum_of_multiples_of_3_or_5(start_num, end_num):
    total = 0
    counter = start_num
    while counter < end_num:
        if is_multiple_of_3(counter) or is_multiple_of_5(counter):
            print(counter)
            total += counter
        counter += 1
    return total


def sum_divisible_by(divisor, less_than):
    p = less_than // divisor
    return divisor * (p*(p+1) // 2)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_for_under_10000000 = sum_of_multiples_of_3_or_5(1, 10000000)
    print(sum_for_under_10000000)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
