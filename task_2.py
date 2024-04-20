import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Checking input parameters
    if not 1 <= min_num <= max_num <= 1000 or not 1 <= quantity <= (max_num - min_num + 1):
        return [] # Введені параметри не відповідають вимогам розіграшу

    # Creating a set to store unique numbers
    uniq_numbers = set()

    # Generation of unique numbers
    while len(uniq_numbers) < quantity:
        uniq_numbers.add(random.randint(min_num, max_num))

    # Returns a sorted list of unique numbers
    return sorted(list(uniq_numbers))

# Run Function
print("Ваші лотерейні числа: ", get_numbers_ticket(1, 49, 6))  # Returns a list of 6 unique numbers in the range 1 to 49
print("Ваші лотерейні числа: ", get_numbers_ticket(1, 36, 5))  # Returns a list of 5 unique numbers in the range 1 to 36
print(get_numbers_ticket(1, 10, 12)) # Wrong parameters
print(get_numbers_ticket(1, 2000, 7)) # Wrong parameters
