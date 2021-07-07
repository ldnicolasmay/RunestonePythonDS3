import re


def anagram_solution_x(str1: str, str2: str) -> bool:

    p = re.compile(r"\W")
    str1_clean = re.sub(p, "", str1.lower())
    str2_clean = re.sub(p, "", str2.lower())

    if len(str1_clean) != len(str2_clean):
        return False

    chars1 = [0] * 26
    chars2 = [0] * 26

    a_int = ord("a")  # 97
    
    for i in range(len(str1_clean)):
        chars1_idx = ord(str1_clean[i]) - a_int
        chars2_idx = ord(str2_clean[i]) - a_int
        chars1[chars1_idx] += 1
        chars2[chars2_idx] += 1

    for i in range(len(chars1)):
        if chars1[i] != chars2[i]:
            return False
    else:
        return True



str1 = "earth"
str2 = "heart"
print(anagram_solution_x(str1, str2))

str1 = "earth"
str2 = "hear"
print(anagram_solution_x(str1, str2))

str1 = "abcd"
str2 = "dbad"
print(anagram_solution_x(str1, str2))

str1 = """
aBcD.,!?;:()[]{}

"""
str2 = """
dbca
"""
print(anagram_solution_x(str1, str2))

str1 = """
To be or not to be: that is the question; whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune...
"""
str2 = """
In one of the Bard's best-thought-of tragedies our insistent hero, Hamlet, queries on two fronts about how life turns rotten.
"""
print(anagram_solution_x(str1, str2))
