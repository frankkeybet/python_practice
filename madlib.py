# Mad Libs Generator with Conditional Statements

print("🎉 Welcome to the Mad Libs Story Generator! 🎉")
print("Let's create a fun and silly story together.\n")

# Step 1: Collect user inputs
day_type = input("Enter an adjective to describe the day (e.g., sunny, rainy, magical): ")
animal1 = input("Enter an animal: ")
animal2 = input("Enter another animal: ")
adjective1 = input("Enter an adjective to describe the first animal: ")
adjective2 = input("Enter an adjective to describe the second animal: ")
verb = input("Enter a verb ending with -ing: ")
emotion = input("Enter an emotion (e.g., happy, scared, amazed): ")

# Step 2: Conditional twist!
if emotion.lower() == "happy":
    reaction = "I couldn’t stop smiling!"
elif emotion.lower() == "scared":
    reaction = "I almost ran away!"
elif emotion.lower() == "amazed":
    reaction = "I stood there in awe, taking it all in."
else:
    reaction = "It was truly an unforgettable feeling."

# Step 3: Build the story
story = f"""
On a beautiful {day_type} day, I went to the zoo. 
I saw a funny {adjective1} {animal1} {verb} in the trees.
Then, I spotted a majestic {adjective2} {animal2} lounging in the sun.
It made me feel so {emotion}! {reaction}
What a wild and {adjective1} experience!
"""

# Step 4: Display the final story
print("\n✨ Your Mad Libs Story ✨")
print(story)
print("Thanks for playing! 🦁🐵")
