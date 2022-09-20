def check_even_list(num_list):
    # return all the even numbers in a list

    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers

check_even_list([1,2,3,4,5])
# [2, 4]
check_even_list([1,3,5])
# []