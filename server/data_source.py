brp_data = []


def generate_dummy_data():
    data_person1 = {'BSN': '830563313', 'surname': 'Jansen', 'initials': 'AJ', 'dateOfBirth': '02-08-1999'}
    data_person2 = {'BSN': '277345108', 'surname': 'Pietersen', 'initials': 'PWA', 'dateOfBirth': '24-12-2001'}

    account_person1 = {'username': 'aj.jansen', 'password': 'foobar'}
    account_person2 = {'username': 'p.pietersen', 'password': 'foobar'}

    brp_data.append({'account': account_person1, 'data': data_person1})
    brp_data.append({'account': account_person2, 'data': data_person2})


def get_data(username):
    print(brp_data)
    for data in brp_data:
        if data['account']['username'] == username:
            return data['data']


def get_date_of_birth(data):
    return data['dateOfBirth']