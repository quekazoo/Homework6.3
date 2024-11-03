def multiply_digits_until_single(number):
    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product
    return number

user_input = int(input("Введіть ціле число: "))
result = multiply_digits_until_single(user_input)
print(result)