print(
    "Instructions -\n 1.) The program will show you the question number, and you will have to type either A/B/C/D/E.... \n 2.) If you wish to not answer a question, leave it blank \n 3.) Once you are done with the test, type 'Q' to exit \n 4.) Your responses will be saved in a text file by the name of the test you enter\n 5.) The options can be changed by entering 'CHANGE', followed by the question number, and then option"
)

test = input("Enter name of the test (no spaces): ")

positive_marking = int(
    input("\nEnter marks alloted for correct answer (without sign): ")
)
negative_marking = int(input("Enter marks deducted for wrong answer (without sign): "))

question_number = 1
answers = {}
print("\n")

# inputting the answers
while True:
    answer = input(f"Enter answer for question number {question_number}: ")
    if answer.lower() == "q":
        break
    if answer.lower() == "change":
        target = int(input("Enter question number: "))
        new_answer = input("Enter new answer: ")
        answers.update({target: new_answer})
    else:
        answers.update({question_number: answer})
        question_number += 1

correct = []
incorrect = []
total_marks = 0
positive_marks = 0
negative_marks = 0

print(
    "\n-----------------------------------------Checking-----------------------------------------\n"
)
for i in range(1, question_number):
    actual_answer = input(f"Enter actual answer for question number {i}: ")
    marked_answer = answers[i]

    if actual_answer.lower() == marked_answer.lower():
        correct.append(i)
        total_marks += positive_marking
        positive_marks += positive_marking

    else:
        incorrect.append(i)
        total_marks -= negative_marking
        negative_marks += negative_marking
print(
    "-----------------------------------------Analysis-----------------------------------------"
)
print(f"Total Marks  = {total_marks}")
print(f"Positive Marks = {positive_marks}")
print(f"Negative Marks = {negative_marks}")

print("\n Correct answers: ")
for i in correct:
    print(i)

print("\n Incorrect answers: ")
for i in incorrect:
    print(i)

print("\n\nWriting data in text file")
file_name = test + ".txt"

with open(file_name, "w") as f:
    f.write("------------------------------------Correct------------------------------------\n")
    for i in correct:
        f.write(f"{i}")

    f.write("-----------------------------------Inorrect-----------------------------------\n")
    for i in incorrect:
        f.write(f"{i}")

    f.write("------------------------------------Analysis------------------------------------")

    f.write(f"\nTotal Marks  = {total_marks}")
    f.write(f"Positive Marks = {positive_marks}")
    f.write(f"Negative Marks = {negative_marks}")
print(f"Wrote data in text file by the name {file_name}")
