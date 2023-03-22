text = input().split()
print(*[word * len(word) for word in text], sep='')
