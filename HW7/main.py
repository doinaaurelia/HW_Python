import user as u
import find
import save
import change_data as ch_data
print(u.add_user_from_txt("new_user.txt"))
# print(u.add_user_from_input())
print(find.find_first_name('Иван'))
print(find.find_last_name('Варова'))
print(find.find_number('+79112223322'))
print(find.find_city('Москва'))
print(ch_data.change_city('+79112223322','Йошкар-Ола'))
save.save("save_users.txt")