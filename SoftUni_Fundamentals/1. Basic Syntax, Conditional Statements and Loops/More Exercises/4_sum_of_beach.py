text = input()
text = text.lower()

my_list = ['sand','water','fish','sun']
counter = 0

for i in my_list:
    if i in text:
        word_count_txt = text.count(i)
        counter += word_count_txt

print(counter)