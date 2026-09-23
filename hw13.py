try:
    f = open("students.txt", "r")

    print("Existing student names:")
    print(f.read())

    f.close()

except FileNotFoundError:
    print("No existing student names.")

n = int(input("How many student names do you want to add? "))
f = open("students.txt", "a")

for i in range(n):
    name = input("Enter student name: ")
    f.write(name + "\n")

f.close()

f = open("students.txt", "r")

print("\nUpdated list of all student names:")
print(f.read())

f.close()