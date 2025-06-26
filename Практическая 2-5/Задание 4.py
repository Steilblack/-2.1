string = input("введите текст: ")
if string.startswith("abc"):
    string = string.replace("abc", "www", 1)
else:
    string += "zzz"
print(string)