# Operations: 
# - create a new record
# - read a record
# - update a record
# - delete a record
# - filter by class
# - export to .csv
# - import from .csv

from cgitb import reset
import re
import format_txt as txt
import format_csv as csv

location = ''
db = []
id_gen = 0

def open_database(filename):
    global location
    global db
    global id_gen
    location = filename
    db = txt.read(filename)
    id_gen = max(list(map(lambda r: int(r[0]), db)), default = 0)

def import_from_csv(filename):
    global location
    global db
    db = csv.read(filename)
    txt.write(location, db)

def export_to_csv(filename):
    global db
    csv.write(filename, db)

def create_record(last_name, first_name, clazz, phone):
    global id_gen
    global db
    global location
    id_gen += 1
    db.append((id_gen, last_name, first_name, clazz, phone))
    txt.write(location, db)

def index_of(id):
    global db
    for i, r in enumerate(db):
        if int(r[0]) == id:
            return i
    return -1
    
def read_record(id):
    global db
    index = index_of(id)
    return db[index] if index >= 0 else None

def update_record(rec):
    global db
    global location
    index = index_of(int(rec[id]))
    if index >= 0:
        db[index] = rec
        txt.write(location, db)

def update_field(id, field, value):
    global db
    global location
    index = index_of(id)
    if index >= 0:
        rec = list(db[index])
        rec[field] = value
        db[index] = tuple(rec)
        txt.write(location, db)

def update_clazz(id, clazz):
    update_field(id, 3, clazz)

def update_phone(id, phone):
    update_field(id, 4, phone)

def delete_record(id):
    global db
    global location
    index = index_of(id)
    if index >= 0:
        db.pop(index)
        txt.write(location, db)

def filter_class(clazz):
    global db
    result = []
    for r in db:
        if r[3] == clazz:
            result.append(r)
    return result

