'''

counties=["Arapahoe", "Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


tempature = int(input("What is the tempature outside?"))

if tempature>80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#(MY CODE)
# what is score?
score=int(input("What is your test score?"))

#determine the grade
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


#(ANSWER KEY)
#what is the score?

score=int(input("What is your test score?"))

#determine the grade
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


#what is the score?
score = int(input("what is your test score?"))

#determine the grade
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >=70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#membership operators
counties = ["Araphoe","Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not the list of counties")


#membership operators + logical operators
counties = ["Arapahoe","Denver", "Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")

'''



