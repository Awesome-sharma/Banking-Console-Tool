# In this task you have to develop a banking console tool in any programming language of your interest.
# This tool will generate a file where the previous 5 transactions of the user are printed in a mini statement
# file. The generated file will be in .csv format. This tool will have the following features:
# ● Tool will generate a .csv formatted file in the current directory.
# ● Tool will take the user name and birth year as input.
# ● Tool will then generate the user_id as per the following example:

# Name: Ryan Reynolds, Birth Year: 1976
# user_id: RYA_REY_1976

# ● You can store dummy data of the transactions for the generation of files.
# ● The tool should fetch the previous 5 transactions of the user and generate the mini statement file.
# ● The file contents should be under the following headings:

# S.N., Date, Time, Amount, Balance
# followed by 5 rows of previous transactions
# ● The name of the file generated should be the same as the user_id.
# ● Tool should be easy to use.


import csv  #impoting necessary libraries

print("***************************************************")
print("*                                                 *")
print("*               Banking Console Tool              *")
print("*                                                 *")
print("***************************************************")
status = "T"
field_names = ["S.N.","Date","Time","Credit/Debit","Amount","Balance"] #field names for the csv file

# Dummy Transaction Data
trans = [
{"S.N.":1,"Date":"01/04/2022","Time":"04:00","Credit/Debit":"Credit","Amount":"1000","Balance":"18000"},
{"S.N.":2,"Date":"05/04/2022","Time":"04:30","Credit/Debit":"Debit","Amount":"2500","Balance":"15500"},
{"S.N.":3,"Date":"07/04/2022","Time":"06:47","Credit/Debit":"Debit","Amount":"500","Balance":"15000"},
{"S.N.":4,"Date":"10/04/2022","Time":"03:20","Credit/Debit":"Credit","Amount":"5000","Balance":"20000"},
{"S.N.":5,"Date":"16/04/2022","Time":"09:00","Credit/Debit":"Debit","Amount":"2500","Balance":"17500"},
]

# Creating Function to make and save csv/excel file in the system
def createcsv(user,trans,field_names):
    user = user+".csv"
    with open(user, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(trans)

# creating function for generating user names
def createusername(name, dob):
    user = ""
    x = 0
    for i in range(len(name)):
        if x < 3:
            user += name[i]
            x += 1
        if name[i] == " ":
            x = 0
            user += "_"
    user += "_"
    user += dob[-4:]
    return user

while status == "T":
    name = input("Give your full name = ")            #taking name of the user or client
    dob = input("Give bate of birth (DD/MM/YYYY) = ") #taking name of the user or client
    user = createusername(name, dob)                  #creating username using the createusername function
    print("Your user name = ", user)
    for i in field_names:
        print(i, "\t", end="")
    print()
    for i in range(len(trans)):
        print(trans[i]["S.N."], "\t", end="")
        print(trans[i]["Date"], "\t", end="")
        print(trans[i]["Time"], "\t", end="")
        print(trans[i]["Credit/Debit"], "\t\t\t", end="")
        print(trans[i]["Amount"], "\t", end="")
        print(trans[i]["Balance"], "\t", end="")
        print()
    createcsv(user, trans, field_names)

    status =input("\nWant details of another user ? \nif yes press 'T', if not press 'F' = ")

print("\nThank you for using our service !!")








