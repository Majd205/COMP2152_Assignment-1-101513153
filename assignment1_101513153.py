"""
Author: Mjd Arow
Assignment: #1
"""

friend_names = ["Alex", "Jamie", "Taylor"]

gym_member = "Alex Alliton"          # string
preferred_weight_kg = 20.5          # float
highest_reps = 25                   # int
membership_active = True            # bool

# Dictionary with string keys and tuple values
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 40)
}

# Add total workout minutes for each friend
for friend in friend_names:
    total = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total

# 2D list (list of lists)
workout_list = [list(workout_stats[friend]) for friend in friend_names]

print("Yoga and running minutes for all friends:", [row[:2] for row in workout_list])
print("Weightlifting minutes for the last two friends:", [row[2] for row in workout_list[-2:]])

for friend in friend_names:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

name = input("Enter friend's name: ").strip().title()

if name in workout_stats:
    yoga, running, weights = workout_stats[name]
    total = workout_stats[f"{name}_Total"]
    print("Yoga:", yoga)
    print("Running:", running)
    print("Weightlifting:", weights)
    print("Total:", total)
else:
    print(f"Friend {name} not found in the records.")

totals = {friend: workout_stats[f"{friend}_Total"] for friend in friend_names}

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("Highest total workout minutes:", highest)
print("Lowest total workout minutes:", lowest)
