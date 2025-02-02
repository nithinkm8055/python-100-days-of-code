len("12345")

print(type("Hello"))
print(type(31))
print(type(123.45))
print(type(True))

print("Number of letters in your name: " + str(len(input("Enter your name"))))
# print(int("123") + "456") # TypeError
print(int("abc") + int("456")) # ValueError