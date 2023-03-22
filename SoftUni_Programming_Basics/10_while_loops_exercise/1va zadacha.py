book_name = input()

search_book = input()

book_cnt = 0

while search_book != "No More Books":
    if search_book == book_name:
        print(f"You checked {book_cnt} books and found it.")
        exit()
    book_cnt += 1
    search_book = input()

print(f"The book you search is not here!")
print(f"You checked {book_cnt} books.")