name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sap = input("Enter SAP ID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")

m1 = int(input("Enter PDS marks: "))
m2 = int(input("Enter Python marks: "))
m3 = int(input("Enter Chemistry marks: "))
m4 = int(input("Enter English marks: "))
m5 = int(input("Enter Physics marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
cgpa = percentage / 10

if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

print("\n----- GRADE SHEET -----")
print("Name:", name)
print("Roll Number:", roll)
print("SAPID:", sap)
print("Sem:", sem)
print("Course:", course)
print("Subject Marks")
print("PDS:", m1)
print("Python:", m2)
print("Chemistry:", m3)
print("English:", m4)
print("Physics:", m5)
print("Percentage:", percentage, "%")
print("CGPA:", round(cgpa, 1))
print("Grade:", grade)

