import numpy as np
import csv  # solved

with open('F:\\1.TESTING\\python\\notes\\py practive.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    fname = []
    for row in csv_file:
        dict_converter = dict(row)
        print(dict_converter)
        f = dict_converter["fname"]
        fname.append(f)
        print(fname)  # addition of first name in list

lname = ["patil", "pawar","kulthe","A"]  # addition of last name in list
domain = "@gmail.com"
fname_total = len(fname)
print(fname_total)  # count of first name in source system
fname_count_variable = fname_total
if fname_total == fname_count_variable:
    print("fname count is", fname_count_variable)
else:
    print("Error")
lname_total = len(lname)  # count of last name in source system
print(lname_total)
mapping_dot = list(map(lambda x, y: x + '.' + y, fname, lname))  # mapping takes place
print(mapping_dot)
email = []  # target system
for i in mapping_dot:
    print(i)
    email_creation = i + domain
    print(email_creation)  # Email id created
    p = len(email_creation)

    # checking the length of email
    if p <= 53:
        print("length of email in target system is perfect")
    else:
        print("not perfect")
    email.append(email_creation)
    print(email)

count_email = len(email)
print(count_email)

# checking source and target count of fname , lname and email
if fname_total == lname_total == count_email:
    print("Working Perfectly")
else:
    print("Not Similar")

# checking the mean value of salary
test_list = [10, 8, 9, 13, 26, 35, 71, 80]
mean_value1 = np.mean(test_list)
print("the avg salary is", mean_value1)