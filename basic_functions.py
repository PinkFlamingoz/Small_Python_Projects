def get_valid_input(type_func, prompt, helper_string1="", num1=-1, helper_string2="", num2=-1):
    while True:

        if helper_string1:
            prompt += " " + helper_string1
        if num1 != -1:
            prompt += " " + str(num1)
        if helper_string2:
            prompt += " " + helper_string2
        if num2 != -1:
            prompt += " " + str(num2) + ":"

        try:
            input_value = type_func(input(prompt))
            return input_value
        except ValueError:
            print("Error: Please enter a valid input. \n")
