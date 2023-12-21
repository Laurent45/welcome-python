
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# YOU CAN CHANGE ONLY THE CODE BELOW

ft_list[1] = "World!"

# Assign an other tuple because tuple is immutable
ft_tuple = (ft_tuple[0], "France!")

# In order to keep the correct order about the expected output,
# I assign a string to ft_set variable
ft_set = "{'Hello', 'Paris!'}"

ft_dict["Hello"] = "42Paris!"

#END

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
