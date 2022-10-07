import user as u

def find_first_name(first_name):
    new_list = []
    for elem in u.users:
        if elem.get('first name') == first_name:
            new_list.append(elem)
    return new_list

def find_last_name(last_name):
    new_list = []
    for elem in u.users:
        if elem.get('last name') == last_name:
            new_list.append(elem)
    return new_list

def find_number(number):
    new_list = []
    for elem in u.users:
        if elem.get('number') == number:
            new_list.append(elem)
    return new_list

def find_city(city):
    new_list = []
    for elem in u.users:
        if elem.get('city') == city:
            new_list.append(elem)
    return new_list