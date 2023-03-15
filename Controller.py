# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.

import Ask
import Functions

def main():
    while True:
        request = Ask.choice()
        if request == 1:
            user = Ask.get_person()
            Functions.write_data(user)
        elif request == 2:
            users = Functions.read_data()
            name = Ask.ask_person()
            Functions.find_person(users, name)
        elif request == 3:
            break
        elif request == 4 or request == 5:
            users = Functions.read_data()
            name = Ask.ask_person()
            List_of_all_Ivans = Functions.output_selected_data(users, name)
            num_str = Ask.ask_num_str()
            Functions.delete_data(List_of_all_Ivans[num_str-1])
            if request == 5:
                new_str = Ask.ask_str()
                Functions.write_data(new_str)
        elif request == 6:
            users = Functions.read_data()
            All_users = [i.strip() for i in users]
            print(All_users)

main()

