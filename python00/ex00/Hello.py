"""
    The purpose of this exercise is to modify the string of each data object
    to display the following greetings:

    $>python Hello.py | cat -e
    ['Hello', 'World!']$
    ('Hello', 'France!')$
    {'Hello', 'Paris!'}$
    {'Hello': '42Paris!'}$
    $>

    You must only modify the lines between #1 and #2
"""

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# 1 YOU CAN CHANGE ONLY THE CODE BELOW

ft_list[1] = "World!"

# Assign another tuple because tuple is immutable
ft_tuple = (ft_tuple[0], "France!")

# In order to keep the correct order about the expected output,
# I assign a string to ft_set variable
ft_set = "{'Hello', 'Paris!'}"

ft_dict["Hello"] = "42Paris!"

# 2 END

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
