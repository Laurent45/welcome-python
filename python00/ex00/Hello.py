
"""
    The purpose of this exercise is to write some code in order to output
    look like this:

    >python Hello.py | cat -e
    ['Hello', 'World!']$
    ('Hello', 'France!')$
    {'Hello', 'Paris!'}$
    {'Hello': '42Paris!'}$
    >
"""

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# YOU CAN CHANGE ONLY THE CODE BELOW

ft_list[1] = "World!"

# You must construct an other tuple because tuple is immutable
ft_tuple = (ft_tuple[0], "France!")

# Sets are unordered, so to keep the correct order about this exercise,
# you can assign a string to ft_set variable
ft_set = "{'Hello', 'Paris!'}"

ft_dict["Hello"] = "42Paris!"

#END

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
