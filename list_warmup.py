# 1. Create a list called fruits with four fruits
fruits = ["Apple", "Banana", "Mango", "Orange"]

# 2. Print the first and the last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Append a fifth fruit, then print the whole list
fruits.append("Grape")
print("After append:", fruits)

# 4. Remove one fruit, then print the list again
fruits.remove("Banana")
print("After remove:", fruits)

# 5. Print how many fruits remain using len()
print("Fruits remaining:", len(fruits))
