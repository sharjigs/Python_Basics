# Bascis
print('hello')
print("hello")

print(" I'm a dog ")

# Indexing
my_string = "abcdefg"

print(my_string)
print('First Index', my_string[0])
print('Last Index', my_string[-1])
print('Middle Index', my_string[1:3])

# Slicing
my_sliceing_string = "asdfghjkl"

print('Beginning:- ', my_sliceing_string[2:])
print('Starting the beginning not including index', my_sliceing_string[:3])
print('Staring and ending point:- ', my_sliceing_string[2:5])
print('Everything:- ', my_sliceing_string[:])
print('Stopr indexing and get next :- ', my_sliceing_string[::2])

# Basic Methods
my_string_methods = "Hello How are you"

print('Upper Case:- ', my_string_methods.upper())
print('Lower Case:- ', my_string_methods.lower())
print('Capitalization:- ', my_string_methods.capitalize())
print('SPLIT:- ', my_string_methods.split())
print('Is Upper Case:- ', my_string_methods.isupper())

# Print Formatting
my_string_print_formationg = 'Insert another string here: {}'.format('Insert ME!')
demo = "Item one: {} Item two: {}".format('Jig', 'poonam')
print(demo)
demo = "Item one: {y} Item two: {x}".format(x='Jig', y='poonam')
print(demo)
print(my_string_print_formationg)

