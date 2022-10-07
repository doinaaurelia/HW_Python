import user as u

def change_city(number, city):
    global users
    for elem in u.users:
        if elem.get('number') == number:
            elem['city'] = city
            return elem