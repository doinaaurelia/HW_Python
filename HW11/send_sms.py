import Person
import Company

def send_sms(*objects):
    for elem in objects:
        number = elem.get_phone()
        if number != None:
            print(f"Отправлено СМС на номер {number} с текстом: {elem.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {elem.get_name()}")
    return None

