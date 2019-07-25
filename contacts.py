#Dictionary Exercise

def add_contact(contacts, name, number):
    if name in contacts.keys():
        print(name, 'kisisi zaten var.')
    else:
        contacts.update({name: number})
        print(name,':', number, 'rehbere eklendi')


def delete_contact(contacts, name):
    try:
        contacts.pop(name)
        print(name, 'rehberden silindi')
    except KeyError:
        print('Kayit Bulunamadi.')


def edit_contact(contacts, name, number):
    try:
        contacts[name]=number
        print(name,'in numarasi ', number, 'olarak guncellendi')
    except KeyError:
        print('Kayit Bulunamadi.')


def find_contact(contacts, name):
    try:
        print(name, ': ', contacts[name])
    except KeyError:
        print('Kayit Bulunamadi.')


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
    6) Cikis''')


contacts={} #dict {name: number}
print_main_menu()
while(True):
    try:
        choice=int(input('Seciminiz: '))
    except ValueError:
        print('Hatali Giris Yaptiniz. Tekrar Deneyin.')
        continue
    if choice==1:
        print_all_contacts(contacts)
    elif choice==2:
        name=input('Isim Girin: ')
        number=int(input('Numara Girin: '))
        add_contact(contacts, name, number)
    elif choice==3:
        name=input('Silinmesini Istediginiz Kisinin Ismini Girin: ')
        delete_contact(contacts, name)
    elif choice==4:
        name=input('Duzenlenecek Kisinin Ismini Girin: ')
        number=int(input('Kisinin Yeni Numarasini Girin: '))
        edit_contact(contacts, name, number)
    elif choice==5:
        name=input('Bulmak Istediginiz Kisinin Ismini Girin: ')
        find_contact(contacts, name)
    else:
        print('Cikis Yapildi.')
        break
