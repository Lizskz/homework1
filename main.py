# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# 1st program
print((9  ** 0.5) * 5)

# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print(result)

# 3rd program
number1 = 1234
number2 = 5678

middle_number1 = (number1 // 10) % 100
middle_number2 = (number2 // 10 ) % 100

sum_of_middles = middle_number1 + middle_number2
print(sum_of_middles)

# 4th program
print(int(13.42 * 100 % 100) == int(42.13) or int(42.13) == int(13.42 * 100 % 100))