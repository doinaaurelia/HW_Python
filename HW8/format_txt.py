def read(filename):
    book = []
    with open (filename + '.txt', 'r') as file:
        for line in file:
            rec = tuple(line.strip().split())
            book.append(rec)
    return book
        
def write(filename, book):
    with open (filename + '.txt', 'w') as file:
        for rec in book:
            id, last_name, first_name, clazz, phone = rec 
            file.write(f'{id} {last_name} {first_name} {clazz} {phone}\n')