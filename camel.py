def camel_to_snake(camel_case):
    snake_case = ''
    for character in camel_case:
        if character.isupper():
           snake_case += '_' + character.lower()
        else:
           snake_case += character
    return snake_case
    

camel_input = input("Please enter name of a variable in camel case: ") # preferredFirstName
snake_output = camel_to_snake(camel_input)
print(snake_output)

