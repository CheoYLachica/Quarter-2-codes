def calculate_fun_sum():

    age_input = input("Hi there! please enter your age: ")
    age = int(age_input)
    cumulative_sum = 0
    for number in range(1, age + 1):
        cumulative_sum += number
    print("The sum of all numbers from 1 to", age, "is", cumulative_sum)

calculate_fun_sum()
