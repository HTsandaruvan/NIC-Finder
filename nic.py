
import datetime
from datetime import date
from calendar import month_name, month

year_no1 =""
year_no2 =""
year_no3 =""
year_no4 =""
date_no1 =""
date_no2 =""
date_no3 =""
birthYear = 0
monthdays = 0
outDate = ""
Date = 0
month = 0
monthName = ""
gender = ""


def getday(days): # find month and day
    match days:
        case 0:
            outDate = "31st of December"
            Date = 31
            month = 12
            monthName = "December"
        case 1:
            outDate = "1st of January"
            Date = 1
            month = 1
            monthName = "January"
        case 2:
            outDate = "2nd of January"
            Date = 2
            month = 1
            monthName = "January"
        case 3:
            outDate = "3rd of January"
            Date = 3
            month = 1
            monthName = "January"
        case 4:
            outDate = "4th of January"
            Date = 4
            month = 1
            monthName = "January"
        case 5:
            outDate = "5th of January"
            Date = 5
            month = 1
            monthName = "January"
        case 6:
            outDate = "6th of January"
            Date = 6
            month = 1
            monthName = "January"
        case 7:
            outDate = "7th of January"
            Date = 7
            month = 1
            monthName = "January"
        case 8:
            outDate = "8th of January"
            Date = 8
            month = 1
            monthName = "January"
        case 9:
            outDate = "9th of January"
            Date = 9
            month = 1
            monthName = "January"
        case 10:
            outDate = "10th of January"
            Date = 10
            month = 1
            monthName = "January"
        case 11:
            outDate = "11th of January"
            Date = 11
            month = 1
            monthName = "January"
        case 12:
            outDate = "12th of January"
            Date = 12
            month = 1
            monthName = "January"
        case 13:
            outDate = "13th of January"
            Date = 13
            month = 1
            monthName = "January"
        case 142:
            outDate = "21st of May"
            Date = 21
            month = 5
            monthName = "May"
        case _ :
            print("Invalid")
    return outDate, Date, month, monthName

def calculateAge(birthDate): # Python3 code to  calculate age in years
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age

nicNo = input("Enter your NIC Number : ") # get NIC number from user
getnic = list(nicNo)

if len(nicNo) == 10: # choose valid NIC No for OLD version
    if nicNo[9]== "v" or nicNo[9]=="V":
        year_no1 = getnic[0]
        year_no2 = getnic[1]
        date_no1 = getnic[2]
        date_no2 = getnic[3]
        date_no3 = getnic[4]

        birthYear = int("1"+"9"+year_no1+year_no2) #get year of Birth

        birthDay = int(date_no1 + date_no2 + date_no3) # find gender
        if birthDay>=500 :
            gender = "Female"
        else :
            gender = "Male"

        birthDay = (int(date_no1+date_no2+date_no3)) % 366 # get day of birth

        outDate,Date,month,monthName = getday(birthDay) #calling get birtdate function
        birth_Year = date(birthYear,month,Date)
        print("your Birhdate is : " + outDate + " and you are " + gender)
        print("You are" ,calculateAge(birth_Year) ,"years")

    else:
        print("Invalid NIC No")

elif len(nicNo)== 12: # choose valid NIC No for NEW version
    year_no1 = getnic[0]
    year_no2 = getnic[1]
    year_no3 = getnic[2]
    year_no4 = getnic[3]
    date_no1 = getnic[4]
    date_no2 = getnic[5]
    date_no3 = getnic[6]

    birthYear = int(year_no1 + year_no2 + year_no3 + year_no4)  # get year of Birth

    birthDay = int(date_no1 + date_no2 + date_no3)  # find gender
    if birthDay >= 500:
        gender = "Female"
    else:
        gender = "Male"

    birthDay = (int(date_no1 + date_no2 + date_no3)) % 366  # get day of birth

    outDate, Date, month, monthName = getday(birthDay)  # calling get birtdate function
    birth_Year = date(birthYear, month, Date)
    print("your Birhdate is : " + outDate + " and you are " + gender)
    print("You are", calculateAge(birth_Year), "years")

else:
    print("invalid")


