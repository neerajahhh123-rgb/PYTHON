name="Anu"
age=20
course="Python Programming"

mark1=85.0
mark2=78.0
mark3=90.0

total=mark1+mark2+mark3
average=total/3
eligible=average>=50


print("----------STUDENT PROFILE----------");
print("Name:",name);
print("Age:",age);
print("Course Name:",course);
print("Subject1 Marks:",mark1);
print("Subject2 Marks:",mark2);
print("Subject3 Marks:",mark3);
print("Total Marks:",total);
print("Average Marks:",round(average,2));
print("Eligible for next level:",eligible);




name="Anu"
age=20
mark=85.0
eligible=True

print("----------DATA TYPES----------");
print("Name:",type(name));
print("Age:",type(age));
print("Mark:",type(mark));
print("Eligible",type(eligible));
