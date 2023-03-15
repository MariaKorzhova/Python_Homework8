def write_data(user):
    """Записывает данные в базу данных"""
    with open("data.txt", "a") as file:
        file.write(user + "\n")



def read_data():
    """Считывет всю информацию в базе данных"""
    with open("data.txt", "r") as file:
        content = file.readlines()
        return content

def find_person(persons, name):
    """По имени или фамилии ищет человека в базе данных"""
    for person in persons:
        if name.lower() in person.lower():
            print(person)


def output_selected_data(users, name):
    """Вывод всех строк, в которых имеются искомые данные"""
    lst = []
    for i in users:
        if name.lower() in i.lower():
            lst.append(i)
            print(len(lst), i)
    return lst

def delete_data(strTODelete):
    with open("data.txt", "r") as file:
        content = file.readlines()
    with open('data.txt', 'w') as file:
        for line in content:
            if line != strTODelete:
                file.write(line)

