Age_of_person= int(input("Enter age: "))
#now we will create if elif else statment
if Age_of_person<=0:
    print("Invalid age")
elif Age_of_person<=2:
    print("Person is baby")
elif Age_of_person>=2 and Age_of_person <4:
    print("person is toddler")
elif Age_of_person>=4 and Age_of_person <13:
    print("person is Kid")
elif Age_of_person>=13 and Age_of_person <20:
    print("person is teenager")
elif Age_of_person>=20 and Age_of_person <65:
    print("person is adult")
elif Age_of_person>=65:
    print("person is elder")
else:
    print("invalid age") #we used else statment for invalid inputs