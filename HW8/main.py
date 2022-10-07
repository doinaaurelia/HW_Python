import students as db

db.open_database('students_base')
# print(db.read_record(5))
# print(db.read_record(3))

# db.create_record('Sokolov', 'Mikhail', '1б', '653')
# db.delete_record(10)
# db.update_phone(2, '111')

class_2b = db.filter_class('2б')
for r in class_2b:
    print(r) 

db.export_to_csv('students_base') 

# for r in db.db:
#     print(r)