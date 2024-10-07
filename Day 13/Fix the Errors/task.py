try:
    age = int(input("How old are you?"))
except:
    print("Use an integer value such as 1,2,3 or 20")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
