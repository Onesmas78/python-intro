#lists - comma separated values enclosed in square brackets
"""
A list is a collection of items in a particular order.
mutable - can be changed after creation
no unique items - can have duplicates
"""

fruits = ["apple", "banana", "cherry"]
# print(fruits) #whole list
# print(fruits[0]) #first item
# fruits.append("orange") #add item to the end
# print(f"Added new item in stock: {fruits}")
# fruits.remove("banana") #remove item
# print(f"Removed item from stock: {fruits}")
# fruits[1] = "kiwi" #change item
# print(f"Changed item in stock: {fruits}")


#tuples - comma separated values enclosed in parentheses
"""
A tuple is an immutable list.
Read-only - cannot be changed after creation
constants - can be used to store constant values
"""
colors = ("#ff0000", "#00ff00", "#0000ff")
# print(f"colors: {colors}")
# print(f"colors[0]: {colors[0]}") #first item
# red,green,blue = colors #tuple unpacking
# print(f"RGB colors: {red},{green},{blue} = {colors}") #tuple unpacking

#dictionaries - key value pairs enclosed in curly braces
"""
A dictionary is a collection of key-value pairs.
"""
person = {"name": "John", "age": 30, "city": "New York"}
# # print(f"person: {person}")
# print(f"person['name']: {person['name']}") #access value by key
# print(f"person['age']: {person['age']}") #access value by key
# print(f"person['city']: {person['city']}") #access value by key

# person["age"] = 31 #change value by key
# print(f"Changed person['age']: {person['age']}") #access value by key
# person["country"] = "USA" #add new key-value pair
# print(f"Added person['country']: {person['country']}") #access value by key
# print(f"person: {person}")

# del person["city"] #remove key-value pair
# print(f"Removed person['city']: {person}") #access value by key

#loops - for, while
"""
A loop is a control flow statement that allows code to be executed repeatedly.
iterable - a collection of items that can be looped over
"""

# for fruit in fruits:
#     print(f"I love {fruit}!")

# for i in range(3): 
#     print(f"i: {i}")

# for i in range(1,10): 
#     print(f"i: {i}")

# for i in range(1,10,2):
#     print(f"i: {i}")

# for i in range(len(fruits)):
#     print(f"fruits: {fruits[i]}")

# for key, value in person.items():
#     print(f"person[{key}]: {value}")

# marks = [90, 80, 70, 60, 50]
# total = 0

# for mark in marks:
#     total += mark

# print(f"Total marks: {total} and the average is: {total/len(marks)}")

#while loop
"""
A while loop is a control flow statement that allows code to be executed repeatedly as long as a condition is true.
break - exit the loop
continue - skip the rest of the code in the loop and go to the next iteration
"""

correct_answer = "42"
while True:
    user_answer = input("What is the answer to life, the universe and everything? ")
    if user_answer == correct_answer:
        print("Correct!")
        break
    else:
        print("Incorrect! Try again.")
        continue