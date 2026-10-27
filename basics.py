

#Variables, types and operators

this_is_a_string = "Hello, World!"   #str
this_is_an_integer = 42             #int - whole number
this_is_a_float = 3.14              #float - single precision decimal number
this_is_a_double = 3.14e10          #double - double precision decimal number
this_is_a_boolean = True            #bool

print(f"Type of this_is_a_string: {type(this_is_a_string)}")
print(f"Type of this_is_an_integer: {type(this_is_an_integer)}")
print(f"Type of this_is_a_float: {type(this_is_a_float)}")
print(f"Type of this_is_a_double: {type(this_is_a_double)}")
print(f"Type of this_is_a_boolean: {type(this_is_a_boolean)}")


#arithmetic operators
a = 10
b = 3
print(f"====== Arithmetic Operators ======")
print(f"a + b = {a + b}")  # addition
print(f"a - b = {a - b}")  # subtraction
print(f"a * b = {a * b}")  # multiplication
print(f"a / b = {a / b}")  # division
print(f"a // b = {a // b}")  # floor division
print(f"a % b = {a % b}")  # modulus 

#reassignment operators
print(f"====== Reassignment Operators ======")
a += 5  # equivalent to a = a + 5
print(f"a += 5 => a = {a}")

#strings methods
my_string = "Hello, World!"
print(f"====== String Methods ======")
print(f"my_string.upper() => {my_string.upper()}")
print(f"my_string.lower() => {my_string.lower()}")
print(f"my_string.title() => {my_string.title()}")
print(f"my_string.len() => {len(my_string)}")
print(f"my_string[5] => {my_string[5]}")
print(f"my_string[7:12] => {my_string[7:12]}")  # slicing


#input methods
user_input = input("Enter something: ")
print(f"You entered: {user_input}")