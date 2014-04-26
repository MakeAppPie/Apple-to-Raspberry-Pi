#python_Strings_demo

my_string ="and now for SOMEthing completely different"
my_silly_string ="silly walks"

pi_value= 3.1415926
integer_value = 123

print (my_string + ' -- The Ministry of ' + my_silly_string )
print (len(my_string))
print (my_string.capitalize())
print (my_string.upper())
print (my_string.lower())
print (my_string.title())
print (my_string.swapcase())


print (my_silly_string.center(30))
print (my_silly_string.center(30,'*'))
print (my_silly_string.rjust(30,'-'))
print (my_silly_string.ljust(30,'^'))
print (my_string.replace('different','penguin'))
print (my_string.partition('SOME'))
print (my_string.count('e'), " e's in our string")
print (my_string.find('e'))
print (
""" ANd now
   for 
something 
           completely 
    different""")
my_string ="Hello {0} {1} {2:5.4g}" .format("Nurse!",12,3.14159)
print(my_string)
