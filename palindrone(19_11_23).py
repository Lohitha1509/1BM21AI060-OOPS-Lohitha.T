# -*- coding: utf-8 -*-
"""palindrone(19-11-23).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wpm-FUf0fXNdvLvGYLTxdXgXdDkIWUVd
"""

def is_palindrome(s):
    return s == s[::-1]

def get_palindromes(input_string):
    palindromes = []
    words = input_string.split()
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)

    return palindromes

input_str = "malayalam is language of kerala"
result = get_palindromes(input_str)
print("Palindromes:", result)