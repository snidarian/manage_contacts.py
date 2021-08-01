#!/usr/bin/python3

# import statements
import sqlite3 # incase needed to interact with sqlite database
import sqlalchemy # to interact with database
from sqlalchemy import text # For writing raw SQL statements in case it's needed
import texttable # to display information to screen
from colorama import Fore, Back, Style, init # to color-highlight information for ease of use and clarity
import os # since this is a terminal program, use of terminal commands will be required
import argparse


# color variable escape sequence definitions
b = Fore.BLUE
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
c = Fore.CYAN
m = Fore.MAGENTA
lb = Fore.LIGHTBLUE_EX
ly = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL


# max table width variable
max_table_width = 105


# Function Definitions

# Generate main menu prompt table
def main_menu_table():
    table_object = texttable.Texttable(0) # zero specifies variable width
    table_object.set_cols_align(["c", "c"])
    table_object.set_cols_valign(["t", "t"])
    table_object.add_rows([
        ["Operation", "Enter Value"],
        ["Exit program", "0"],
        ["View Contact(s)", "1"],
        ["Create Contact(s)", "2"],
        ["Update contact(s)", "3"],
        ["Delete Contact(s)", "4"]])
    print(ly)
    print(table_object.draw())
    print(reset)

# Generate update menu table (Which column of selected record to update)
def generate_update_menu_table():
    table_object = texttable.Texttable(0) # zero specifies variable width
    table_object.set_cols_align(["c", "c"])
    table_object.set_cols_valign(["t", "t"])
    print("Enter value to update (0 to quit to main menu)")
    table_object.add_rows([
        ["Operation", "Entry Value"],
        ["Firstname", "1"],
        ["Lastname", "2"],
        ["Sex", "3"],
        ["Phone", "4"],
        ["email", "5"],
        ["Address", "6"],
        ["Description", "7"],
        ["Where met", "8"]])
    print(ly)
    print(table_object.draw())
    print(reset)


def print_contacts_table():
    os.system('clear')
    table_object = texttable.Texttable(max_table_width)
    table_object.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c"])
    table_object.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t"])
    table_object.set_cols_dtype(["t", "t", "t", "t", "t", "t", "t", "t", "t", ])
    selection_object = contacts.select()
    result = connection_object.execute(selection_object)
    #record = result.fetchone()
    table_object.header(["Id", "Firstname", "Lastname", "Sex", "Phone", "Email", "Address", "Description", "Where met"])
    for row in result:
        table_object.add_row( [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])] )
    # draw and print table
    print(table_object.draw())


def generate_table_and_print(rows_list):
    table_object = texttable.Texttable(max_table_width) # variable size 0
    table_object.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c"])
    table_object.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t"])
    table_object.set_cols_dtype(["t", "t", "t", "t", "t", "t", "t", "t", "t", ])
    table_object.header(["id", "Firstname", "Lastname", "Sex", "Phone", "Email", "Address", "Description", "Where met"])
    for row in rows_list:
        table_object.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
    print(table_object.draw())

# Get single record and generate table for single record
def select_table_single_record(selection_id):
    table_object = texttable.Texttable(max_table_width)
    table_object.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c"])
    table_object.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t"])
    table_object.set_cols_dtype(["t", "t", "t", "t", "t", "t", "t", "t", "t", ])
    table_object.header(["id", "Firstname", "Lastname", "Sex", "Phone", "Email", "Address", "Description", "Where met"])
    # Create selection object that target desired record called for with parameter
    selection_object = text("SELECT * FROM contacts WHERE contacts.id = :x")
    result = connection_object.execute(selection_object, x = str(selection_id)).fetchone()
    table_object.add_row([result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]])
    print(table_object.draw())


# Main menu entry prompt function
def main_menu():
    inputvar=""
    os.system('clear')
    try:
        while inputvar != "0":
            main_menu_table()
            print(lb)
            inputvar = input("--> ")
            print(reset)
            if inputvar == '0':
                break
            elif inputvar == '1':
                select_record()
            elif inputvar == '2':
                insert_record()
                os.system('clear')
            elif inputvar == '3':
                update_record()
            elif inputvar == '4':
                delete_record()
    except KeyboardInterrupt:
        print("Program terminated from keyboard")


# CRUD FUNCTION DEFINITIONS


# evaluates each variable to determine if it's a string 0 or not - returns True or False
def insert_return_to_main_menu(variable):
    if variable == "0":
        return False
    else:
        return True

# INSERT
def insert_record():
    run=True
    while run == True:
        print("Enter 0 at any prompt to return to the Main menu")
        firstname = input("Firstname: ")
        run = insert_return_to_main_menu(firstname)
        if run == False:
            break
        lastname = input("Lastname: ")
        run = insert_return_to_main_menu(lastname)
        if run == False:
            break
        sex = input("Sex (m/f): ")
        run = insert_return_to_main_menu(sex)
        if run == False:
            break
        phone = input("Phone #: ")
        run = insert_return_to_main_menu(phone)
        if run == False:
            break
        email = input("Email Address: ")
        run = insert_return_to_main_menu(email)
        if run == False:
            break
        address = input("Physical Address: ")
        run = insert_return_to_main_menu(address)
        if run == False:
            break
        description = input("Description of contact: ")
        run = insert_return_to_main_menu(description)
        if run == False:
            break
        where_met = input("Where you first met: ")
        run = insert_return_to_main_menu(where_met)
        if run == False:
            break

        # take values and generate contact-entry dictionary
        record_dict = { 
            'firstname' : str(firstname), 
            'lastname' : str(lastname), 
            'sex' : str(sex), 
            'phone' : str(phone),
            'email' : str(email),
            'address' : str(address),
            'description' : str(description),
            'where_met' : str(where_met)
            }

        #print("Record dictionary:")
        #print(record_dict)

        # Execute insert statement:
        connection_object.execute(contacts.insert(), record_dict)


# SELECT
def select_record():
    select_all = input("Select all contacts? " + ly + "(y/n): " + reset)
    select_all = select_all.upper()
    if select_all == 'Y':
        print_contacts_table()
    elif select_all == 'N':
        print(lb)
        print("SQL wilcards: '%' = *, '_' = . ")
        regex = input('SQL regex--> ')
        print(reset)
        os.system('clear')
        selection_object = text("SELECT * FROM contacts WHERE contacts.firstname or contacts.lastname LIKE :x")
        result = connection_object.execute(selection_object, x = str(regex)).fetchall()
        generate_table_and_print(result)
    else:
        print("Error: Invalid selection...")
        os.system('sleep 2')
# UPDATE
def update_record():
    run = True
    while run == True:
        os.system('clear')
        print_contacts_table()
        print(w + "Type id of record to update (0 to return to main menu)" + reset)
        selection_id = input(g + "--> " + reset)
        os.system('clear')
        try:
            if selection_id == "0":
                break
            elif int(selection_id) > 0:
                select_table_single_record(selection_id) # function - draw table with single record and print
                generate_update_menu_table() # update menu table
                updatevar = input(w + "Enter value to update (0 to quit)\n" + g + "--> " + reset)
            try:
                if int(updatevar) == 0:
                    break
                elif int(updatevar) == 1:
                    new_value = input("Enter new firstname value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(firstname=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 2:
                    new_value = input("Enter new lastname value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(lastname=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 3:
                    new_value = input("Enter new sex value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(sex=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 4:
                    new_value = input("Enter new phone value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(phone=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 5:
                    new_value = input("Enter new email value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(email=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 6:
                    new_value = input("Enter new address value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(address=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 7:
                    new_value = input("Enter new description value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(description=new_value)
                    connection_object.execute(update_object)
                elif int(updatevar) == 8:
                    new_value = input("Enter new 'where met' value: ")
                    update_object = contacts.update().where(contacts.c.id==selection_id).values(where_met=new_value)
                    connection_object.execute(update_object)
                else:
                    print("Error: Invalid Entry")
            except:
                print("Error: Invalid Entry")
                os.system('sleep 2')
        except:
            print("Error: Invalid Entry")
            os.system('sleep 2')
        


# DELETE
def delete_record():
    id_selection = 1.5
    while int(id_selection) > 0:
        print_contacts_table()
        id_selection= input(w + "Enter id of record to delete (0 to quit):\n" + g + "--> " + reset)
        deletion_object = contacts.delete().where(contacts.c.id==id_selection)
        # delete specified record
        connection_object.execute(deletion_object)
    os.system('clear')


# ---------------------------------------------------------------------------------
# PROGRAM SETUP


# Set up and parse database arguement

parser = argparse.ArgumentParser(description="Manages contacts from encrypted persistent DB file")
# program takes one arguemnt - filepath to database file to manage
args = parser.add_argument("database", help="SQLite database file path", type=str)

# prepare argument for use
args = parser.parse_args()



# Initiate connection with database 

# create engine
from sqlalchemy import create_engine
engine = create_engine("sqlite:///{}".format(args.database), echo=False)


# generate connection object - creates database in question if not already created
connection_object = engine.connect()


# Set up Metadata class
from sqlalchemy import MetaData
# alias for Metadataclass class
Meta = MetaData()

# set up primary Table 'contacts'
from sqlalchemy import Table, Column, Integer, String

# set up contacts table
contacts = Table(
    'contacts', Meta,
    Column('id', Integer, primary_key = True),
    Column('firstname', String),
    Column('lastname', String),
    Column("sex", String),
    Column('phone', String),
    Column('email', String),
    Column('address', String),
    Column('description', String),
    Column('where_met', String)
)

# Execute the creation of the Table 'contacts'
Meta.create_all(engine)



# -------------------------------------------------------------------------------------
# EXECUTIONS


if __name__=="__main__":
    print("mark0")
    print("interacting with database: " + args.database) # database
    main_menu()
    











