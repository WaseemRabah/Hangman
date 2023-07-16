import random
from words import fruits
random_word = random.choice(fruits)
print(random_word)
hidden_word = '_' * len(random_word)
print(hidden_word)