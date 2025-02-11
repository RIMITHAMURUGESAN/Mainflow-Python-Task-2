def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

s = input("Enter a string: ")
v, c = count_vowels_consonants(s)
print("Vowels:", v)
print("Consonants:", c)
