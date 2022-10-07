import user as u

def save(file_name):
    with open(file_name, 'a') as f:
        for elem in u.users:
            first_name = elem.get('first name')
            last_name = elem.get('last name')
            number = elem.get('number')
            city = elem.get('city')
            f.write(f"{first_name}\n{last_name}\n{number}\n{city}\n\n")