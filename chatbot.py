def remind_name():
    name = input("Hi! What's your name? ")
    print(f"Nice to meet you, {name}!")

def guess_age():
    print("Enter remainders of your age divided by 3, 5, and 7.")
    r3 = int(input("Remainder mod 3: "))
    r5 = int(input("Remainder mod 5: "))
    r7 = int(input("Remainder mod 7: "))
    age = (r3 * 70 + r5 * 21 + r7 * 15) % 105
    print(f"Your age is {age}! That's a great age to learn Python.")

def count():
    num = int(input("Enter a number and I will count up to it: "))
    for i in range(num + 1):
        print(f"{i}!")

def test():
    print("Why do we use functions?")
    print("1. Repeat code")
    print("2. Break code into smaller parts")
    print("3. Print output")
    print("4. Stop program")
    while int(input("Choose 1-4: ")) != 2:
        print("Try again.")
    print("Correct!")

def end():
    print("Thanks for chatting. Have a great day!")

# Run chatbot
remind_name()
guess_age()
count()
test()
end()





def greet():
    print("👋 Hello! Welcome to our service feedback chatbot.")

def get_user_info():
    name = input("What's your name? ")
    age = input("How old are you? ")
    print(f"Nice to meet you, {name}!")

def get_experience():
    exp = input("How was your overall experience with us? (e.g., good, average, poor): ")
    print(f"Thank you for your response: {exp.capitalize()}.")

def get_rating():
    print("Please rate our service (1 to 5 stars):")
    rating = int(input("Your rating: "))
    if rating == 5:
        print("🌟🌟🌟🌟🌟 Excellent! We're glad you loved it.")
    elif rating >= 3:
        print("🌟🌟🌟 Thanks! We’ll keep improving.")
    else:
        print("😟 Sorry to hear that. We’ll try to do better.")

def get_feedback():
    more = input("Would you like to give any additional feedback? (yes/no): ").lower()
    if more == "yes":
        feedback = input("Please type your feedback here: ")
        print("🙏 Thanks for sharing your thoughts!")
    else:
        print("No problem! Thanks for your time.")

def end():
    print("✅ Your feedback has been recorded. Have a great day!")

# Run chatbot
greet()
get_user_info()
get_experience()
get_rating()
get_feedback()
end()
