strings = input().split()
searched_palindrome = input()
palindromes = []

for word in strings:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
