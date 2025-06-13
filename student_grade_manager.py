# This is a simple programme that records student names and their associated grades, aswell as the class average
school_class = []


def student_tracker():
    total = 0
    count = 0

    # Takes in the size of the call
    size = input("How many students are in the class? ")
    print("\n")

    # Append the names and grades onto a list
    while count < int(size):
        names = input(f"What is the name of the student {count + 1}? ")
        grade = int(input("What was their grade? "))
        print("\n")
        school_class.append({"names": names, "grade": grade})
        count = count + 1

    # Print the names and grades onto the screen
    for e in school_class:
        print(f"{e['names']} - {e['grade']}")

    # Iterate through the grades, add them together and get the average
    for e in school_class:
        total += e['grade']
        average_grade = total / count
    print("the average grade is ", average_grade)


if __name__ == "__main__":

    while True:
        decision = input("Would you like to record grades? Yes or No ")

        if decision == "Yes":
            student_tracker()
        elif decision == "No":
            print("Thanks")
            break
        else:
            print("That is not a valid input, please type 'Yes' or 'No'")
