# COMP2152 - Assignment 1

## <u>Details</u>

Individual assignment

<u>Code Instructions</u>

1. Create a new file called **assignment1_studentID.ipynb** (This is a Jupyter Notebook python file - this type of file is created automatically when you create a new file in Jupyter Notebook on GBLearn)
   1. Add a multi-line comment at the top of the file with the following lines of data:
      - Author: \<YOUR REAL FIRST AND LAST NAME\>
      - Assignment: #1
   2. Create 4 variables:
      - Add a 1-line comment for each variable with its corresponding data types commented to the right.
        - `gym_member = "Alex Alliton"`
        - `preferred_weight_kg = 20.5`
        - `highest_reps = 25`
        - `membership_active = True`
   3. Create a dictionary named **`workout_stats`** with the following structure:
      - **Keys**: Strings representing the names of friends (e.g., "Alex", "Jamie", "Taylor").
      - **Values**: Tuples containing three integers representing the number of minutes spent on three different workout activities (e.g., **`(30, 45, 20)`** for yoga, running, and weightlifting).
      - Add a 1-line comment above the dictionary explaining its data type.
   4. Using a loop, calculate the total workout minutes for each friend. Add new key-value pairs in the dictionary for each friend. For the key, use something like "Alex_Total", and for the value, use the calculated total minutes.
   5. Create a 2-dimensional (nested) list called **`workout_list`** by extracting all the workout minutes from the dictionary. Each row should represent a friend, and each column should represent one activity (yoga, running, or weightlifting). Add a 1-line comment explaining its data type.
   6. Slice the **`workout_list`** to:
      - Extract and print the minutes for yoga and running for all friends.
      - Extract and print the minutes for weightlifting for the last two friends.
   7. Use an if-statement within a loop to:
      - Check if any friend's total workout minutes are greater than or equal to 120.
      - If true, print their name and the message: **`"Great job staying active, <friend_name>!"`**
   8. Add a feature to allow the user to input a friend's name. Check if the name exists in the dictionary:
      - If it exists, print the friend's workout minutes for each activity and their total workout minutes.
      - If it doesn't exist, print a message: **`"Friend <name> not found in the records."`**
   9. Include a section at the end of your program where you print:
      - The friend with the highest total workout minutes.
      - The friend with the lowest total workout minutes.

2. Follow the instructions in the **first-contributions** repository README file
   1. [https://github.com/mmurphy-gbc/first-contributions](https://github.com/mmurphy-gbc/first-contributions)

## <u>Submission instructions</u>

### Submission Items

1. **Code**: Upload a single code file called **assignment1_studentID.ipynb**

2. **5 Screenshots required** (Can also be .jpg files):
   1. **gitClone**.png
   2. **gitBranch.**png
   3. **gitCheckout.**png
   4. **gitCommit.**png
   5. **gitPush**.png

### Submission Locations

Unless specified below, upload all six items above

1. **Github under your account**
   1. Note: Only the screenshots of your git will be checked. Your repository won't be checked directly. Please follow academic honesty!

2. **GBLearn** running a Jupyter Labs IDE
   1. **Note**: If you missed Lab Week 3, make sure to look there for instructions to download Jupyter Labs on GBLearn
   2. Upload your code under **public_html/python/jupyter/comp2152/assignments/assignment1**

3. **D2L**
   1. Zip up your **assignment1_studentID.ipynb** and submit as **assignment1_studentID.zip**
   2. Submit all 5 screenshots, unzipped, directly onto D2L
