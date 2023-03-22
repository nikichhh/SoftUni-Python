string_one = input()
string_two = input()
for i in range(len(string_one)):
  
  if string_one[i] != string_two[i]:

    string_one = string_one[:i] + string_two[i] + string_one[i + 1:]
    print(string_one)