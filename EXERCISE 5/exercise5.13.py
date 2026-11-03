# menghitung nilai dan menentukan predikat berdasarkan nilai yang diperoleh
name = "Djilva"
score = 85

print("STUDENT GRADE CALCULATOR")
print("-----------------------")
print(f"Student Name: {name}")
print(f"Student Score: {score}")

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Great job!")
elif score >= 70:
    print("Grade: C")
    print("Keep improving!")
elif score >= 60:
    print("Grade: D")
    print("You need more practice.")
else:
    print("Grade: E")
    print("Please study harder.")