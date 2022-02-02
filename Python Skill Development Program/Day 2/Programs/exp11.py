# Name - Rudraksh Karpe
# Roll No.- SCOB86
age = 50
id= [1, 2, 3, 4, 5]

emp_name=["Ram", "Preethi", "Rahul", "Abhijeet"]

num_emp = 4

emp_list = [id, emp_name, num_emp]

print("Before:")
print(emp_list)

emp_age=[43,45,47,49]
emp_list.append(emp_age)
print("After:")
print(emp_list)

del(emp_list[2])

print("After deletion:")
print(emp_list)
