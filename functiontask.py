# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


def calculate_total_and_average(maths, eng, swa, sci, sos):
    total = maths + eng + swa + sci + sos
    average = total / 5
    return total, average

# Function to determine grade based on average marks
def determine_grade(average):
    if average > 79:
        return 'A'
    elif 60 <= average <= 79:
        return 'B'
    elif 50 <= average <= 59:
        return 'C'
    elif 40 <= average <= 49:
        return 'D'
    else:
        return 'E'


try:
    maths = int(input("Enter marks for Maths: "))
    eng = int(input("Enter marks for English: "))
    swa = int(input("Enter marks for Swahili: "))
    sci = int(input("Enter marks for Science: "))
    sos = int(input("Enter marks for Social Studies: "))

    # Calculate total and average
    total, average = calculate_total_and_average(maths, eng, swa, sci, sos)

    # Determine grade
    grade = determine_grade(average)

    # Display results
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

except ValueError:
    print("Please enter valid integer marks for all subjects.")