
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
print("Original list:", random_numbers)
even_numbers = []
for num in random_numbers:
    if num % 2 == 0:
        even_numbers.append(num * 2)
print("Modified list (even numbers doubled):", even_numbers)