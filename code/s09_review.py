if score >= 90:
    print("You got an A")
elif score >= 60:
    print("You passed")
else:
    print("Fail")


def evaluate_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
score = int(input("Enter your score: "))
result = evaluate_score(score)
print(result)

def mystery(x):
    if x > 0:
        return "Positive"
print("done")

result = mystery(5)
print(result)

x = 15
y = x > 10 and x < 200
print(type(y))
print(y)

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
#Test cases
# print(is_leap_year(2026))  # True
# print(is_leap_year(2027))  # True
## print(is_leap_year(2023))  # False
## print(is_leap_year(1900))  # False
## print(is_leap_year(2000))  # True

# how to find the next leap year after a given year?

def check(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} is divisible by both 2 and 3")
    elif n % 2 == 0:
        print(f"{n} is divisible by 2 but not by 3")
    else:
        print(f"{n} is not divisible by 2")

check(8)
check(6)


i = 0
while i < 5:
    print(i)
    i += 1

#Example: Input validation loop
print("\n----Input Validation Example----")
valid_input = False
while not valid_input:
    age= int(input("Enter your age (must be 0-120)"))
    age_num=int(age)
    if 0 <= age_num <= 120:
        valid_input = True
        print(f"Valid age: {age_num}")
        valid_input = True
    else:
        print("Age must be between 0 and 120. Try again.")

#Example: Simple Login System
print("\n----Simple Login System----")
username = "admin"
password = "password123"

while True:
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input == username and pass_input == password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Please try again.")

def game_loop():
    print(game on....)
    return "game over"

while True:
    result = game_loop()
    if result == "game over":
        break


words = ["hello", "world", "target", "python"]
for w in words:
    print('checking:', w)
    if w == "target":
        print("Found it!")
        continue
    print("Not the target\n")

for num in range(18):
    if num % 2 == 0:
        continue
    print(num) # prints and numbers only

def f(n):
    for num in range(n):
        if num % 2 == 0:
            continue
        print(num)

# print(f(10)) # prints odd numbers from 0 to 9

