# -*- coding: utf-8 -*-
import sys
import os
import csv

class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts  = []

    def add(self, name,phone,email):
        contact  = Contact(name,phone,email)
        self._contacts.append(contact)
        self.save()
        # print('nombre{}\ntelefono{}\nemail{}'.format(name,phone,email))

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    
    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- *')

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                # borrar  
                del self._contacts[idx]
                print('Contacto eliminado!')
                self.save()
                break
    
    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else: 
            self.not_found()
    
    def update(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                newName  = input('Ingresa el nuevo nombre del contacto:\n')
                newPhone = input('Ingresa el nuevo telefono del contacto:\n')
                newEmail = input('Ingresa el nuevo email del contacto:\n')
                contact.name  =  newName
                contact.phone  = newPhone
                contact.email  = newEmail
                print('!Contacto modificado correctamente!')
                self.save()
                break
        else:
            self.not_found()

    def not_found(self):
        print('***********')
        print('Contacto no encontrado')
        print('***********')

    def save(self):
        with open ('contacts.csv', 'w') as f:
            writer  = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone,contact.email))

def run():
    contact_book  = ContactBook()
    # vamos a leer el archivo
    with open('contacts.csv','r') as f :
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if row == []:
                continue
            contact_book.add(row[0],row[1],row[2])

    while True:
        command = input('''
        ¿Qué deseas hacer?

        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        ''')

        if(command == 'a' or command =='A'):
            os.system('cls')
            print('**** AÑADIR CONTACTO ****')
            name  = input('Digita el nombre del contacto:\n')
            phone = input('Digita el telefono del contacto:\n')
            email = input('Digita el email del contacto:\n')
            contact_book.add(name,phone,email)


        elif(command =='ac' or command== 'AC'):
            os.system('cls')
            print('**** ACTUALIZAR CONTACTO ****')
            name = input('Digita el nombre del contacto a actulizar\n')
            contact_book.update(name)
        
        elif(command == 'b' or command=='B'):
            os.system('cls')
            print('**** BUSCAR CONTACTO ****')
            name = input('Digita el nombre del contacto a buscar\n')
            contact_book.search(name)
        
        elif(command =='e' or command == 'e'):
            os.system('cls')
            print('**** ELIMINAR CONTACTO ****')
            name = input('Digita el nombre del contacto a eliminar\n')
            contact_book.delete(name)
        
        elif(command=='l' or command=='L'):
            os.system('cls')
            print('**** LISTA DE CONTACTOS ****')
            contact_book.show_all()
        
        elif (command=='s' or command=='S'):
            sys.exit()
        else:
            print('**** COMANDO NO VALIDO ****')

if __name__ == '__main__':
    run()