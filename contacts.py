# Dictionary Exercise (Basic Contacts App)

from os import system

def add_contact(contacts, name, number):
    if name in contacts.keys():
        print(name, 'kisisi zaten var.')
    else:
        contacts.update({name: number})
        print(name,':', number, 'rehbere eklendi.')


def delete_contact(contacts, name):
    try:
        contacts.pop(name)
        print(name, 'rehberden silindi.')
    except KeyError:
        print('Kayit bulunamadi.')


def edit_contact(contacts, name, number):
    try:
        contacts[name]=number
        print(name,'in numarasi ', number, 'olarak guncellendi.')
    except KeyError:
        print('Kayit bulunamadi.')


def find_contact(contacts, name):
    print(name, ': ', contacts.get(name,'Kayit bulunamadi.'))


def print_all_contacts(contacts):
    for name, number in contacts.items():
        print(name, ':', number)


def print_main_menu():
    print('''
Telefon Rehberi Uygulamasina Hosgeldiniz.
Lutfen Yapmak Istediginiz Islemi Secin:
    1) Rehberi Goruntule
    2) Kayit Ekle
    3) Kayit Sil
    4) Kayit Duzenle
    5) Rehberde Bul
    6) Cikis\n''')


def input_number(message):
    while True:
        try:
            number=int(input(message))
        except ValueError:
            print('Numara rakamlardan olusmalidir.')
            continue
        break
    return number


contacts={} # dict {name: number}
system('clear')
print_main_menu()
while(True):
    try:
        choice=int(input('\nSeciminiz: '))
    except ValueError:
        print('Hatali giris yaptiniz. Tekrar deneyin.')
        continue
    if choice==1:
        system('clear')
        print_main_menu()
        print_all_contacts(contacts)
    elif choice==2:
        name=input('Isim Girin: ')
        number=input_number('Numara Girin: ')
        system('clear')
        print_main_menu()
        add_contact(contacts, name, number)
    elif choice==3:
        name=input('Silinmesini Istediginiz Kisinin Ismini Girin: ')
        system('clear')
        print_main_menu()
        delete_contact(contacts, name)
    elif choice==4:
        name=input('Duzenlenecek Kisinin Ismini Girin: ')
        number=input_number('Kisinin Yeni Numarasini Girin: ')
        system('clear')
        print_main_menu()
        edit_contact(contacts, name, number)
    elif choice==5:
        name=input('Bulmak Istediginiz Kisinin Ismini Girin: ')
        system('clear')
        print_main_menu()
        find_contact(contacts, name)
    else:
        system('clear')
        print_main_menu()
        print('Cikis Yapildi.')
        break

# Alperen Cubuk