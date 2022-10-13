import Person, Company, send_sms

person1 = Person.Person("Ivan", "Ivanovich", "Ivanov", {"private":123, "work":456})
person2 = Person.Person("Ivan", "Petrovich", "Petrov", {"private":789})
person3 = Person.Person("Ivan", "Petrovich", "Sidorov", {"work":789})
person4 = Person.Person("John", "Unknown", "Doe", {})
company1 = Company.Company("Bell", "OOO", {"contact":111}, person3, person4)
company2 = Company.Company("Cell", "AO", {"non_contact":222}, person2, person3)
company3 = Company.Company("Dell", "Ltd", {"non_contact":333}, person2, person4)
send_sms.send_sms(person1, person2, person3, person4, company1, company2, company3)

print()
print()
person1 = Person.Person("Степан", "Петрович", "Джобсов", {"private":555})
person2 = Person.Person("Боря", "Иванович", "Гейтсов", {"private":777, "work":888})
person3 = Person.Person("Семен", "Робертович", "Возняцкий", {"work":789})
person4 = Person.Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company.Company("Яблочный комбинат", "OOO", {"contact":111}, person1, person4)
company2 = Company.Company("ПластОкно", "AO", {"non_contact":222}, person2)
company3 = Company.Company("Пингвинья ферма", "Ltd", {"non_contact":333}, person4)
send_sms.send_sms(person1, person2, person3, person4, company1, company2, company3)





