class Person():
    def __init__(self,first_name, dad_s_name, last_name, numbers):
        self.first_name = first_name
        self.dad_s_name = dad_s_name
        self.last_name = last_name
        self.numbers = numbers
    
    def get_phone(self):
        return self.numbers.get("private")

    def get_name(self):
        fio = self.last_name + " " + self.first_name + " " + self.dad_s_name 
        return fio

    def get_work_phone(self):
        return self.numbers.get("work")
    
    def get_sms_text(self):
        return f"Уважаемый {self.first_name} {self.dad_s_name }! Примите участие в нашем беспроигрышном конкурсе для физических лиц"