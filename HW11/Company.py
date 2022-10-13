import Person
class Company:
    def __init__(self, name, type, numbers, *persons):
        self.name = name
        self.type = type
        self.numbers = numbers
        self.list = persons

    def get_phone(self):
        if self.numbers.get("contact") != None:
            return self.numbers.get("contact")
        else:
            for person in self.list:
                if person.get_work_phone() != None:
                    return person.get_work_phone()
                    break
        return None

    def get_name(self):
        return self.name
    
    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.type}"