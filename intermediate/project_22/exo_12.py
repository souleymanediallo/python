import string
import random


letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

generated_letters = ''.join(random.choices(letters, k=5))
generated_numbers = ''.join(random.choices(numbers, k=5))
generated_punctuation = ''.join(random.choices(punctuation, k=5))

print(generated_letters)
print(generated_numbers)
print(generated_punctuation)

