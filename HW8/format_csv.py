def read(filename):
    book = []
    with open (filename + '.csv', 'r') as file:
        next(file) # Пропускаем заголовок
        for line in file:
            rec = tuple(line.strip().split(';'))
            book.append(rec)
    return book
        
def write(filename, book):
    with open (filename + '.csv', 'w') as file:
        file.write('id;фамилия;имя;класс;телефон\n')
        for rec in book:
            id, last_name, first_name, clazz, phone = rec 
            file.write(f'{id};{last_name};{first_name};{clazz};{phone}\n')