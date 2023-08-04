def get_valid_input(type_func, prompt, helper_string1="", num1=-1, helper_string2="", num2=-1, optional=False):
    while True:

        if helper_string1:
            prompt += " " + helper_string1
        if num1 != -1:
            prompt += " " + str(num1)
        if helper_string2:
            prompt += " " + helper_string2
        if num2 != -1:
            prompt += " " + str(num2) + ":"

        user_input = input(prompt)
        if optional and user_input == '':
            return None

        try:
            input_value = type_func(user_input)
            return input_value
        except ValueError:
            print("Error: Please enter a valid input. \n")
