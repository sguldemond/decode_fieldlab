import time
import datetime

# utils to check for age and stuff

def ageCheck(age, dateOfBirth):
    print(time.mktime(datetime.datetime.strptime(dateOfBirth, '%d-%m-%Y').timetuple()))


ageCheck(18, '03-08-1999')