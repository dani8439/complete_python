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

# Tuple unpacking

stock_prices = [('APPL',200), ('GOOG',400), ('MSFT',100)]
for item in stock_prices:
    print(item)

# ('APPL', 200)
# ('GOOG', 400)
# ('MSFT', 100)

for ticker,price in stock_prices:
    print(ticker)
# APPL
# GOOG
# MSFT

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        # keep comparing through list of tuples, and switching when it's higher
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Return tuple 
    return (employee_of_month, current_max)

employee_check(work_hours)
# ('Cassie', 800)