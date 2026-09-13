age = int(input("How old are you? "))

if age < 18:
    print("You are not an adult")
else:
    print("You are an adult")

birth_year = int(input("What year were you born? "))
age = 2025 - birth_year

print("Your age is", age)