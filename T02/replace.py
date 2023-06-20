# program to replace a "!" sign with spaces in sentences
single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
single_string_replaced = single_string.replace("!", " ")
print(single_string_replaced) # printing out the above replaced string without !
print(single_string_replaced.upper()) #all upper cases
print(single_string_replaced[::-1]) # sentence in reverse