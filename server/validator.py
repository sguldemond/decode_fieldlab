import time
import datetime

# utils to check for age and stuff

# TODO: fix age difference with one day?
def age_check(age, date_of_birth):
    current_time_utc = time.time()
    print(current_time_utc)

    user_time = time.mktime(datetime.datetime.strptime(date_of_birth, "%d-%m-%Y").timetuple())
    print(user_time)

    print(current_time_utc - user_time)

    min = datetime.datetime.fromtimestamp(user_time)
    max = datetime.datetime.fromtimestamp(current_time_utc)

    print("Total days : " + str((max - min).days))

    # input_time = datetime.strptime(date_of_birth, '%d-%m-%Y')
    # print(input_time)


def check(request, user_data):
    if user_data is None:
        return "No user data found"

    if request == 'ouderdan18':
        print(user_data)
        if user_data['dateOfBirth'] == "02-08-1999":
            return True
        if user_data['dateOfBirth'] == "24-12-2001":
            return False

    return "Request not found"


age_check(18, '03-08-1999')
