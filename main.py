def show_menu():
    print('1. Распечатать справочник', 
          '2. Найти телефон по фамилии', 
          '3. Добавить абонента в справочник', 
          '4. Изменить контакт', 
          '5. Удалить контакт',
          '6. Найти телефон по номеру телефону',  
          '0. Закончить работу', sep='\n')
    choice = input()
    return choice

def work_with_phonebook():	
    choice = show_menu()
    phone_book = read_txt('phon.txt')
    while (choice != '0'):
        if choice == '1':
            print_contacts(phone_book)
        elif choice == '2':
            lastname = input('Введите фамилию: ')
            find_number_lastname(phone_book, lastname)
        elif choice == '3':
            add_phone_number('phon.txt')
        elif choice == '4':
            lastname = input('Введите фамилию: ')
            edit_contact(phone_book, lastname)
        elif choice == '5':
            lastname = input('Введите фамилию: ')
            delete_by_lastname(phone_book, lastname)
        elif choice == '6':
            telnum =input('Введите номер телефона: ')
            find_number_telnum(phone_book, telnum)
        elif not choice.isdigit() or int(choice) > 6:
            print('Неправильно выбрана команда!')
            print()          
        choice=show_menu()

def read_txt(file_name):
    result_list = []
    fields =  [' Фамилия', ' Имя', ' Номер телефона', ' Описание',]
    with open(file_name,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))     
            result_list.append(record)	
    return result_list


def write_txt(filename , phone_book):
    with open(filename,'w',encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = '' 
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}')


def find_number_lastname(contact_list, last_name):
    found_contacts = []
    for contact in contact_list:
        if contact[' Фамилия'] == last_name:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()

def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value}', end='')
            print()

def get_new_number():
    last_name = input('Введите фамилию: ') + ','
    first_name = input('Введите имя: ') + ','
    phone_number = input('Введите номер телефона: ') + ','
    description = input('Введите описание: ')
    return last_name, first_name, phone_number, description, 

def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'\n{info}')

def find_contact_for_changing(phnb_1st, last_name):
    find_1st = [] 
    for i in range(len(phnb_1st)):
        if phnb_1st[i][' Фамилия'] == last_name:
            find_1st.append(i)
    if len(find_1st) != 0:
        if len(find_1st)>1:
            print("Найдено несколько контактов с такой фамилией, необходимо уточнить номер телефона для\n")
            print_contacts([phnb_1st[cont_ind] for cont_ind in find_1st])
            num = input("Введите номер телефона для уточнения: ")
            not_find_num = True
            for cont_ind in find_1st:
                if phnb_1st[cont_ind][' Номер телефона'] == num:
                    not_find_num = False
                    return cont_ind
            if not_find_num:
                return 'Контакта с таким номером телефока нет'
        else:
                return find_1st[0]
    else:
        return 'Контакта с такой фамилией в отобранном списке нет'

def edit_contact(phnb_lst, last_name):
    cont_ind=find_contact_for_changing(phnb_lst, last_name)
    if type(cont_ind) == str:
        print(cont_ind)
    else:
        print_contacts([phnb_lst[cont_ind]])
        choice = show_edit_menu()
        fields = [' Фамилия', ' Имя', ' Телефон', ' Описание']
        edit = False
        edited_contact = phnb_lst[cont_ind].copy ()
        while choice not in [5,6]:
            k = fields[choice-1]
            new_data = input(f'{k}: ')
            edited_contact[k]=new_data
            edit = True
            choice = show_edit_menu()

        if choice == 5 and edit == True:
            print("Контакт изменен")
            phnb_lst[cont_ind] = edited_contact
            write_txt("phon.txt", phnb_lst)
        
def show_edit_menu():
    print('1. Фамилия',
          '2. Имя',
          '3. Телефон',
          '4. Описание',
          '5. Подтвердить изменения',
          '6. Отменить изменения', sep = '\n')
    choice=int(input("Введите команду: "))
    return choice

def delete_by_lastname(phnb_lst,last_name):
    cont_ind=find_contact_for_changing(phnb_lst,last_name)
    if type(cont_ind) == str:
        print(cont_ind)
    else:
        print_contacts([phnb_lst[cont_ind]])
        delete=''
        while delete not in ['да','нет']:
            delete=input("Подтвердите удаление данного контакта - напечатайте да или нет: ")
        if delete == 'да':
            phnb_lst.pop(cont_ind)
            write_txt("phon.txt", phnb_lst)
            print("Данный контакт удален\n")

def find_number_telnum(phone_book, telnum):
    found_contacts = []
    for contact in phone_book:
        if contact[' Номер телефона'] == telnum:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()

work_with_phonebook()