"""
College Computer Science (A Level)

Allowed time: 10 minutes

Starter coding task:

Write a Python program that asks the user to enter a word or short string.

Leading and trailing whitespace should be ignored.

The program should determine whether all remaining characters in the input are unique.

If duplicate characters exist, display:

* Each character that appears more than once.
* All positions where that character appears, using positions starting from 1.

Example:

Input:
banana

Output:
The string does not contain only unique characters as it contains multiple copies of the following characters:

the character a which is found at positions 2, 4, and 6
the character n which is found at positions 3 and 5

If there are no duplicate characters, display:

The string contains only unique characters.
"""

from collections import defaultdict

while True:
    word = input("> Input a word: ")

    word = word.strip()

    if len(set(word)) == len(word):
        print("The string contains only unique characters")
        continue

    mapping = defaultdict(list)

    for i, char in enumerate(word, start=1):
        mapping[char].append(i)
        
    filtered = {
        char: val 
        for char, val in mapping.items()
        if len(val) > 1
    }

    print(
        "The string does not contain only unique characters "
        "as it contains multiple copies of the following characters:\n"
    )

    for char, val in filtered.items():
        val = val.copy()
        end = val.pop()
        print(f"the character {char} which is found at positions {", ".join(map(str, val))}, and {end}")

