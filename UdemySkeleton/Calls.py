from Teacher import Teacher

List1 = []
for i in range(4):
    name = input("Enter the teacher's name: ")
    subject = input("Enter the teacher's subject: ")
    List1.append(Teacher(name, subject))

for i in List1:
    print(i)
