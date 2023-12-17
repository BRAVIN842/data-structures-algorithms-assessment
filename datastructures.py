# Question 1: Balanced Expressions

def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return False

    return not stack

# example
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

# Question 2: Remove Duplicates

def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# example
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

# Question 3: Word Frequency

import re

def word_frequency(sentence):
    frequency_dict = {}
    words = re.findall(r'\b\w+\b', sentence.lower())

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# example
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
