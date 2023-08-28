#!/usr/bin/env python3

# Question 1
def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers


input_list = [0, 1, 3, 5, 7, 8, 9]
result = return_evens(input_list)
print(result)  # Output: [0, 8]


# Question 2
def make_exclamation(sentences):
    exclamation_sentences = [sentence + "!" for sentence in sentences]
    return exclamation_sentences

input_sentences = ["Hello", "I'm doing great", "Python is fun"]
result = make_exclamation(input_sentences)
print(result)
