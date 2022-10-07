users = []


def user(first_name, last_name, number, city):
    return {'first name': first_name, 'last name': last_name, 'number': number, 'city': city}


def add_user_from_txt(file_name):
    global users
    with open(file_name, "r") as f:
        new_str = " "
        while new_str != "":
            new_str = f.readline()
            first_name = new_str[:len(new_str)-1]
            new_str = f.readline()
            last_name = new_str[:len(new_str)-1]
            new_str = f.readline()
            number = new_str[:len(new_str)-1]
            new_str = f.readline()
            city = new_str[:len(new_str)-1]
            new_str = f.readline()
            users.append(user(first_name, last_name, number, city))
    return users


def add_user_from_input():
    global users
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    number = input("Введите номер: ")
    city = input("Введите город проживания: ")
    users.append(user(first_name, last_name, number, city))
    return users